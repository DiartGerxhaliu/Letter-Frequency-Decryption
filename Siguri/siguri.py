from collections import Counter
import string
import re

# English letter frequency (most common → least common)
english_freq_order = "ETNIAOSRHLDCUMFGPYBWVXQKZJ"

# read original text and keep its spacing/punctuation
original_text = input("Enter text: ").upper()

# keep only letters for frequency analysis
letter_text = "".join([c for c in original_text if c in string.ascii_uppercase])

# count letters
counts = Counter(letter_text)

# sort by frequency
sorted_counts = counts.most_common()

print("Letter counts:")
for letter, count in sorted_counts:
    print(f"{letter}: {count}")

# build frequency order from the text
cipher_order = "".join([letter for letter, _ in sorted_counts])

print("\nCipher frequency order:")
print(cipher_order)

print("\nEnglish frequency order:")
print(english_freq_order)

# create substitution guess for letters only
mapping = {}
for i, letter in enumerate(cipher_order):
    if i < len(english_freq_order):
        mapping[letter] = english_freq_order[i]

print("\nSuggested substitution:")
for k, v in mapping.items():
    print(f"{k} -> {v}")


def apply_mapping(text, mapping):
    return "".join([mapping.get(c, c) for c in text])


def show_mapping(mapping):
    if not mapping:
        print("(no mappings)")
        return
    for k in sorted(mapping.keys()):
        print(f"{k} -> {mapping[k]}")


# initial decode
decoded = apply_mapping(original_text, mapping)

# interactive loop: let user edit mapping until they say No
while True:
    print("\nDecoded guess:")
    print(decoded)
    ans = input("\nDo you want to edit the frequency:(Yes, No, Show): ").strip().lower()
    if ans in ("no", "n"):
        print("\nProgram end")
        break
    if ans in ("show",):
        print("\nSuggested substitutions:")
        show_mapping(mapping)
        print("\nDecoded guess:")
        print(decoded)
        continue
    if ans in ("yes", "y"):
        while True:
            edit = input("What do you wanna edit (Ex. A->M), or 'done' to finish: ").strip()
            if edit.lower() == "done":
                print("Change(s) applied.")
                break
            m = re.match(r'^\s*([A-Za-z])->([A-Za-z])\s*$', edit)
            if not m:
                print("Invalid format. Use A->M or 'done'.")
                continue
            src = m.group(1).upper()
            tgt = m.group(2).upper()
            
            changed_keys = set()
            
            # Check if src is a decoded letter (mapping value) - priority to decoded text
            keys_to_update = [k for k, v in mapping.items() if v == src]
            if keys_to_update:
                for k in keys_to_update:
                    mapping[k] = tgt
                    changed_keys.add(k)
                print(f"Change made: {', '.join(keys_to_update)} -> {tgt}")
            elif src in mapping:
                # src is a cipher letter (key) in the mapping
                mapping[src] = tgt
                changed_keys.add(src)
                print(f"Change made: {src} -> {tgt}")
            else:
                # src not recognized; treat as new cipher letter
                mapping[src] = tgt
                changed_keys.add(src)
                print(f"Change made: {src} -> {tgt} (new)")
            
            # update decoded text immediately after each change
            decoded = apply_mapping(original_text, mapping)
            print("\nUpdated decoded text:")
            print(decoded)
            
            # Check if another cipher letter already maps to this target and reassign it
            # (excluding the keys we just changed)
            existing_sources = [k for k, v in mapping.items() if v == tgt and k not in changed_keys]
            if existing_sources:
                # Find available letters not already in use as targets
                taken_targets = set(mapping.values())
                available = [c for c in string.ascii_uppercase if c not in taken_targets]
                
                for old_src in existing_sources:
                    if available:
                        new_tgt = available.pop(0)
                        mapping[old_src] = new_tgt
                        print(f"Reassigned: {old_src} -> {new_tgt} (was pointing to {tgt})")
                    else:
                        # Remove if no available letters
                        del mapping[old_src]
                        print(f"Removed: {old_src} (was pointing to {tgt}, no available letters)")
                # update again after reassignments
                decoded = apply_mapping(original_text, mapping)
                print("\nCorrected decoded text:")
                print(decoded)
        continue
    print("Please answer Yes, No, or Show.")