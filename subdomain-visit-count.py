class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # create a counter variable to count the occurences of each cpdomain
        counter = defaultdict(int)

        # count the occurences of each cpdomain
        for cpdomain in cpdomains:
            # extract the domain and the occurence
            occerences, domain = cpdomain.split()
            occerences = int(occerences)

            # increment the count of each subdomain
            counter[domain] += occerences
            for i in range(len(domain)):
                if domain[i] == '.':
                    counter[domain[i+1:]] += occerences

        # convert the dictionary to a list
        res = []
        for subdomain, count in counter.items():
            res.append(f'{count} {subdomain}')

        return res

        
