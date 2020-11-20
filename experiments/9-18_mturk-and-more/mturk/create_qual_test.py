import argparse
import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
MTURK_PROD = 'https://mturk-requester.us-east-1.amazonaws.com'
AWS_ACCESS_KEY_ID = 'AKIAIRPYZDF4EZVIJSBQ'  # TODO: fill in.
AWS_SECRET_ACCESS_KEY = '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'  # TODO: fill in.


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--version',
		default='sandbox',
		type=str,
		required=False,
		help='Either `sandbox` or `prod`.'
	)

	args = parser.parse_args()
	print('args', args)

	# Set global variables.
	if args.version == 'prod':
		endpoint_url = MTURK_PROD
	elif args.version == 'sandbox':
		endpoint_url = MTURK_SANDBOX
	else:
		raise NotImplementedError('args.version has to be sandbox or prod')

	# Set up mturk client.
	mturk = boto3.client('mturk',
	                     region_name='us-east-1',
	                     endpoint_url=endpoint_url,
	                     aws_access_key_id=AWS_ACCESS_KEY_ID,
	                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my account")

	# Make pretest.
	#make_qual_test(mturk)


if __name__ == '__main__':
	main()
