# Recme plugin for Errbot

[Errbot](http://errbot.net) is a Python-based bot. This is is a plugin for
Errbot that allows chat users to create recommendations.

## Installation

To install the plugin, tell your bot in a private chat:

```
!repos install https://github.com/alimac/err-recme.git
```

## Configuration

There is nothing to configure, yet.

## Interaction

This plugin allows your bot to store and return recommendations (recs). Recme
makes use of [Flows](http://errbot.io/en/latest/user_guide/flow_development/)
to engage in a very basic conversation.

### Add a new rec

```
!recme new
Oooh! A new rec? Tell me everything!
Klingon dictionary is exciting
Okay, @alimac. I saved this rec.
```


### Ask for a rec

To have the bot give you a random recommendation:

```
!recme random
Klingon dictionary is exciting
```

To list all recommendations:

```
!recme all
Klingon dictionary is exciting
The _Never Ending Sacrifice_ is an epic tale spanning seven generations of the history of a Cardassian family which displayed selfless obedience to Cardassia.
Everyone should read Ferengi Rules of Acquisition
```

### Remove a rec

Not supported yet.

## Caveats

I literally just started working on this plugin, so it will go through many
changes and refactors.
