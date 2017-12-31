import random
from errbot import botcmd, BotPlugin, botmatch


class Recme(BotPlugin):

    recme_store = []

    @botcmd
    def recme_new(self, msg, _):
        """Start to guess a number !"""
        return 'Oooh! A new rec? Tell me everything!'

    @botmatch(r'^.+$', flow_only=True)
    def recme_save(self, msg, match):

        if 'RECME' in self:
            self.recme_store = self['RECME']

        self.recme_store.append(match.string)
        self['RECME'] = self.recme_store

        yield "Okay, {}. I saved this rec." .format(msg.frm)

    @botcmd
    def recme_all(self, message, args):
        """ List all recs """

        if 'RECME' in self:
            self.recme_store = self['RECME']

        if self.recme_store:
            for rec in self.recme_store:
                yield rec

        else:
            yield "No recs yet. *!recme new* to add one"

    @botcmd
    def recme_random(self, message, args):
        """ Return random rec """

        if 'RECME' in self:
            self.recme_store = self['RECME']

        if self.recme_store:
            yield random.choice(self.recme_store)

        else:
            yield "No recs yet. *!recme new* to add one"
