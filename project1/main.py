import redactor
import argparse

if __name__== '__main__':
    parser = argparse.ArgumentParser(description='Text Analytics Project1')
    parser.add_argument("--input", type=str, required=True, help="Input Files", nargs='*', action='append')
    parser.add_argument("--names", required=False, help="Redact_names", action='store_true')
    parser.add_argument("--gender", required=False, help="Redact_genders", action='store_true')
    parser.add_argument("--dates", required=False, help="Redact_dates", action='store_true')
    parser.add_argument("--stats", required=False, help="Redacted_stats", action='store_true')
    parser.add_argument("--concept", type=str, required=False, help="Redacting concept words")
    parser.add_argument("--output", type=str, required=True, help="Output Files")

    args = parser.parse_args()

    a = redactor.Reading_input(args.input)

    if (args.names):
         a = redactor.redact_names(a)
    if (args.gender):
         a = redactor.redact_gender(a)
    if (args.dates):
         a = redactor.redact_date(a)
    if (args.concept):
         a = redactor.redact_concept(a, args.concept)
    if (args.output):
        redactor.Update_Output(args.input, a, args.output)
    if (args.stats):
        redactor.Update_Redacted_stats()
