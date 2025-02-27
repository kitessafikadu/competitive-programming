# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain  = cpdomain.split()
            count = int(count)

            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])

                count_map[subdomain] += count
        
        return [f"{count} {domain}" for domain, count in count_map.items()]