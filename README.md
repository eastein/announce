<A name="toc1-0" title="Mission: Announcable" />
# Mission: Announcable

Voiceovers. Informative soundbites. Say it with emphasis and a somewhat below-par text to speech engine.

<A name="toc1-5" title="Networked Announcer Daemon: announced" />
# Networked Announcer Daemon: announced

The announce daemon, **announced**, takes 2 arguments: one, a URL to bind to for ZeroMQ SUB, and optionally a filename to a json file full of text to filename mappings.  For example

    [
      ["hello world", "helloworld.mp3"],
      ["flee for your lives, puny mortals.", "flee.mp3"]
    ]

In this case, if those files are in the working directory from which **announced** was invoked, if strings matching (or close-enough, read the code if you care how the close-enough logic works, it's pretty simple) the first part of each mapping are sent, then the text to speech engine will be skipped and the files will be played instead.

Messages sent to the **announced** daemon have 2 required arguments: `text` and `pitch`.  Pitch is currently not used when a file is matched.

    import zmqsub
    spk = zmqsub.JSONZMQConnectPub('tcp://*:4900')
    spk.send({'text': 'flee for your lives, puny mortals', 'pitch' : 0})

The above example would cause the `flee.mp3` file to be played back.
