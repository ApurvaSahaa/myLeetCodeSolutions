class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []

        for email in emails:
            names = email.split("@")
            #localname
            localname = ''.join(names[0].split("+")[0].split("."))
            #domainname
            domainname = names[1]
            fullemail = f'{localname}@{domainname}'
            if fullemail not in res:
                res.append(fullemail)
        return len(res)