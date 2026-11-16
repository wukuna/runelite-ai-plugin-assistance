"""Advisory RuneLite source scan. Read-only; findings require contextual review."""
import argparse
import json
import re
from pathlib import Path

RULES = [
    ("packager-candidate", "direct-audio-api", r"javax\.sound|\b(?:AudioSystem|AudioInputStream|AudioFormat|SourceDataLine)\b"),
    ("prohibited-candidate", "focus-manager", r"\bKeyboardFocusManager\b"),
    ("prohibited-candidate", "runtime-process-native", r"\b(?:Runtime\b|ProcessBuilder|System\s*\.\s*load(?:Library)?\s*\(|com\.sun\.jna|org\.lwjgl|native\s+\w+\s+\w+\s*\()"),
    ("prohibited-candidate", "reflection", r"java\.lang\.reflect|\b(?:getDeclared(?:Field|Fields|Method|Methods|Constructor|Constructors)|getField|getFields|getMethod|getMethods|getConstructor|getConstructors|setAccessible|trySetAccessible|Class\s*\.\s*forName)\s*\("),
    ("prohibited-candidate", "thread-sleep-interrupt", r"\bThread\s*(?:\.|::)\s*(?:sleep|interrupt)\b|\.\s*interrupt\s*\("),
    ("prohibited-candidate", "own-json-http-client", r"\bnew\s+(?:(?:com\.google\.gson\.)?(?:Gson|GsonBuilder)|(?:okhttp3\.)?OkHttpClient(?:\s*\.\s*Builder)?)\s*\("),
    ("prohibited-candidate", "unapproved-network-client", r"\b(?:HttpURLConnection|URLConnection|Socket|ServerSocket)\b|java\.net\.http|\.\s*openConnection\s*\("),
    ("prohibited-candidate", "plugin-package", r"\bpackage\s+net\.runelite(?:\.|\s*;)"),
    ("prohibited-candidate", "direct-file-api", r"java\.io\.(?:File|FileReader|FileWriter|FileInputStream|FileOutputStream|RandomAccessFile)(?:\s*;|\b)|java\.nio\.file\.(?:Files|Paths)\b|\b(?:Files|Paths)\s*\."),
    ("review-candidate", "desktop-opening", r"\bDesktop\b|\bLinkBrowser\s*(?:\.|::)\s*open\b"),
    ("review-candidate", "menu-action-exception", r"\.\s*menuAction\s*\("),
    ("sensitive", "client-script", r"\.\s*runScript\s*\("),
    ("restricted", "world-hop-unchecked-packets", r"\.\s*hopToWorld\s*\(|\bFilepath\s*\.\s*Unchecked\b|\.\s*setCanSendPackets\s*\("),
    ("reviewer-observed", "management-env-invoke", r"java\.lang\.management|javax\.management|com\.sun\.management|\bSystem\s*\.\s*getenv\s*\(|\b(?:VarHandle|MethodHandles)\b"),
    ("review-candidate", "indirect-interruption", r"\.\s*shutdownNow\s*\(|\.\s*cancel\s*\(\s*true\s*\)"),
    ("packager-candidate", "legacy-widget-account-api", r"\b(?:WidgetInfo|WidgetID|AccountClient|AccountSession|SessionManager)\b"),
    ("review-candidate", "resource-file-assumption", r"\.\s*getResource\s*\("),
]
LEXEMES = re.compile(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|//[^\r\n]*|/\*[\s\S]*?\*/')


def strip_noncode(source):
    # Preserve line numbers while avoiding comments/string-literal false positives.
    return LEXEMES.sub(lambda m: re.sub(r"[^\r\n]", " ", m.group()), source)


def scan(repository, include_tests=False):
    repository = Path(repository).resolve(strict=True)
    roots = [("production", repository / "src/main")]
    if include_tests:
        roots.append(("test-only", repository / "src/test"))
    findings = []
    count = 0
    for scope, root in roots:
        if not root.is_dir():
            continue
        for file in sorted(root.rglob("*")):
            if file.suffix in (".kt", ".scala"):
                findings.append(dict(scope=scope, category="prohibited-candidate", rule="non-java", file=str(file.relative_to(repository)), line=1))
            if file.suffix != ".java":
                continue
            count += 1
            source = file.read_text(encoding="utf-8-sig")
            code = strip_noncode(source)
            for category, rule, pattern in RULES:
                for match in re.finditer(pattern, code):
                    line = code.count("\n", 0, match.start()) + 1
                    key = (scope, rule, str(file), line)
                    if any((f["scope"], f["rule"], str(repository / f["file"]), f["line"]) == key for f in findings):
                        continue
                    findings.append(dict(scope=scope, category=category, rule=rule, file=str(file.relative_to(repository)), line=line))
    if not (repository / "src/main").is_dir():
        raise ValueError("No src/main directory; this scanner requires the standard source layout.")
    return dict(repository=str(repository), java_files=count, findings=findings,
                limitations="Advisory lexical scan, not a compliance certificate. Review test-only findings separately. Does not inspect dependencies, resolve types, count bot tokens, or validate gameplay behavior.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    parser.add_argument("--include-tests", action="store_true")
    args = parser.parse_args()
    print(json.dumps(scan(args.repository, args.include_tests), indent=2))


if __name__ == "__main__":
    main()
