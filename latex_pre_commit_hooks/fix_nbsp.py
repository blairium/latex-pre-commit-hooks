import sys


def replace_nbsp(filenames):
    # The hex code for a non-breaking space is \xa0
    target = "\xa0"
    replacement = " "

    for filename in filenames:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            if target in content:
                # Replace all instances of \xa0 with a standard space
                new_content = content.replace(target, replacement)

                with open(filename, "w", encoding="utf-8", newline="") as f:
                    f.write(new_content)
                print(f"Removed non-breaking spaces (NBSP) in: {filename}")
            else:
                # No NBSPs found in this file
                pass

        except Exception as e:
            print(f"Error processing {filename}: {e}")


def main():
    if len(sys.argv) > 1:
        replace_nbsp(sys.argv[1:])


if __name__ == "__main__":
    main()
