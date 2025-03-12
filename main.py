
import argparse
import run
def parse_args():
    parser = argparse.ArgumentParser(description='Test LLM model')
    parser.add_argument('--model', choices=['llama', 'gpt'], default=None, nargs='+', help='Usable LLM model lists')
    parser.add_argument('--option', choices=['basic', 'rag', 'chat'], type=str, default=None, help='option')
    parser.add_argument('--question_path', default=None, help='Usable LLM model lists')


    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    print('[LOGGING] You chose the following LLM model: %s' %(str(', '.join(args.model))))
    runner = run.Runner(model_names=args.model,
                        option=args.option)

if __name__ == '__main__':
    main()

