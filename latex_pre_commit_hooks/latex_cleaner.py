import re
import sys


def clean_latex(filenames):
    # 1. Matches \cite{...} across lines, including NBSPs (\xa0)
    cite_content_regex = re.compile(r"\\cite\{([\s\S]*?)\}")

    # 2. Matches [not tilde or newline or opening bracket] followed by \cref
    cref_spacing_regex = re.compile(r"([^~\n\(\[])\\cref")

    # 3. Matches ( followed by any number of spaces or tildes then \cref
    # This targets "( \cref" and "(~\cref"
    cref_parenthesis_cleanup = re.compile(r"\([\s~]+\\cref")

    for filename in filenames:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Step A: Clean internal citation whitespace
            def fix_cite_internal(match):
                keys = match.group(1)
                cleaned_keys = re.sub(r"[\s\xa0]+", "", keys)
                return f"\\cite{{{cleaned_keys}}}"

            new_content = cite_content_regex.sub(fix_cite_internal, content)

            # Step B1: Specific Cleanup - Remove space/tilde after opening parenthesis
            # "( \cref" -> "(\cref"
            new_content = cref_parenthesis_cleanup.sub(r"(\\cref", new_content)

            # Step B2: General Spacing - Ensure ~ before \cref
            # (unless it's preceded by a newline, tilde, (, or [)
            new_content = cref_spacing_regex.sub(r"\1~\\cref", new_content)

            if content != new_content:
                with open(filename, "w", encoding="utf-8", newline="") as f:
                    f.write(new_content)
                print(f"Refined LaTeX spacing in: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")


def main():
    clean_latex(sys.argv[1:])


if __name__ == "__main__":
    main()
