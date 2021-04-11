import redactor
import argparse

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Files to be redacted.")
    parser.add_argument("--names", help="Redact names", action='store_true')
    parser.add_argument("--dates", help="Redact dates", action='store_true')
    parser.add_argument("--phones",help="Redact phones", action='store_true')
    parser.add_argument("--stats", help="Statistics of redacted types", action='store_true')
    parser.add_argument("--concept", type=str, required=False, help="to redact the given concept words")
    parser.add_argument("--output", type=str, required=True, help="Redacted Output Files")

    args = parser.parse_args()

    temp = redactor.Read_files(args.input)

    if (args.names):
         temp = redactor.sanitize_names(temp)
    if (args.gender):
         temp = redactor.sanitize_phones(temp)
    if (args.dates):
         temp = redactor.sanitize_dates(temp)
    if (args.concept):
         temp = redactor.sanitize_concepts(temp, args.concept)
    if (args.output):
        redactor.final_output(args.input, temp, args.output)
    if (args.stats):
        redactor.update_statlist()

