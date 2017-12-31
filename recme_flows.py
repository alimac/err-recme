from errbot import botflow, FlowRoot, BotFlow, FLOW_END


class RecmeFlows(BotFlow):
    """ Conversation flows related to polls"""

    @botflow
    def recme(self, flow: FlowRoot):
        """ This is a flow that can take book recs."""
        # setup Flow
        rec = flow.connect('recme_new', auto_trigger=True)
        rec.connect('recme_save')
