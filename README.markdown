IDEONE.py
=========

A simple wrapper for the ideone.com SOAP API for Python using SOAPpy

    ideone = IdeOne()

    # run a python program
    python = 116
    link = ideone.createSubmission("print('Hello World')\n", python)

    # wait for it to finish 
    while ideone.getSubmissionStatus(link)[0] != Status.Done:
        pass

    # print output
    print ideone.getSubmissionDetails(link)['output']
