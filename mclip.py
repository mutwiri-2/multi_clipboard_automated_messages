#! python3
# mclip.py - store and easily copy multiple messages to your computer's clipboard 

TEXT = {
    'reminder': '''Hey <customers' name>, quick reminder about your meeting tomorrow with <employee name> at <address>''',
    'subscribe': '''Hi <name>, thanks for opting in for SMS updates from <your company>! You can text STOP at any time to unsubscribe''',
    'status-alert': '''Hello <name>, this is <employee name> from <your company>. We are still working on your order, but we expect that it will be complete by <date>. Please text back if you have any questions!''',
    'agree': '''Yes, I agree. That sounds fine to me''',
    'busy': '''Sorry. Can we do this later this week or next week kindly.'''
}

import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py[keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1]  # second command-line argument is the keyphrase