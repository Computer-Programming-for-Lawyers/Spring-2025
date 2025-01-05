# Turns justices.txt data (cut-and-pasted from https://www.supremecourt.gov/about/members_text.aspx)
# into a CSV

# Just redirect this into new file from command line.

# First processing chiefs, then associates
title = "Chief Justice"

for row in open('justices.txt'):
    row = row.strip()
    if row.startswith('#'):
            continue
    elif row == "":
            continue
    elif row == "Chief Justices":
            continue
    elif row == "Associate Justices":
            title = "Associate Justice"
            continue
    elif row.startswith("Name\t"):
            continue

    # Made it this far, has data
    fields = row.split('\t')
    # Currently sitting justices have only 4 fields
    if len(fields) < 5:
        fields.append('')
    fields.append(title)
    print (';'.join(fields))
