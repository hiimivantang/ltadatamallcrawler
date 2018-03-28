import requests
import sys
import os
from optparse import OptionParser,OptionGroup
from config import settings


class SelectedMode:
    def __init__(self, selected_api, options=None):
        self.headers = dict(AccountKey=settings['ltadatamall']['key'],UniqueUserId=settings['ltadatamall']['guuid'],Accept='application/json')
        self.selected_api = selected_api
        self.options = options
        self.url = settings['urls'][selected_api]['url']
        self.frequency = settings['urls'][selected_api]['frequency']

    def describe(self):
        print("API: %s" %self.selected_api)

    def getdata(self):
        try:
            return requests.get(self.url, headers=self.headers).text
        except Exception as e:
            sys.stderr.write('%s\n'%e.message)
        return None


def main():
    parser = OptionParser()
    group = OptionGroup(parser, 'Available APIs', 'Please select one!')
    for api_desc in settings['urls'].keys():
        group.add_option('--%s' %(api_desc), const=api_desc, dest="mode", action='store_const')

    parser.add_option_group(group)
    (opts, args) = parser.parse_args()
    if opts.mode is None:
        sys.stderr.write('Please select API. Use -h to see the available options.\n')
        return

    selectedmode = SelectedMode(opts.mode)

    # print(selectedmode.url)
    # print(selectedmode.frequency)
    # print(selectedmode.headers)
    import json
    from pprint import pprint
    pprint(json.loads(selectedmode.getdata()))


if __name__ == '__main__':
    main()



