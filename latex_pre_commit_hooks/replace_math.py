import re
import sys


def replace_math(filenames):
    # Updated Regex:
    # (?<!\$)      - Negative lookbehind: No $ before
    # \$           - Starting $
    # (?!\()       - Negative lookahead: DO NOT match if next char is ( [TikZ check]
    # ([^$\n]+?)   - Capture group: Anything not a $ or newline
    # \$           - Ending $
    # (?!\$)       - Negative lookahead: No $ after
    inline_regex = re.compile(r"(?<!\$)\$(?!\()([^$\n]+?)\$(?!\$)")

    for filename in filenames:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace $...$ with \( ... \)
            new_content = inline_regex.sub(r"\\(\1\\)", content)

            if content != new_content:
                with open(filename, "w", encoding="utf-8", newline="") as f:
                    f.write(new_content)
                print(f"Fixed math delimiters (ignoring TikZ) in: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")


def main():
    replace_math(sys.argv[1:])


if __name__ == "__main__":
    main()
