class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            email_cleaned = self.clean(email)
            s.add(email_cleaned)

        return len(s)

    def clean(self, email):
        email = email.lower()
        local, domain = email.split('@')
        local = local.replace('.', '')
        local = local.split('+')[0]
        return local + '@' + domain

