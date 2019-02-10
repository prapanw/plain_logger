from Logger.Logger import Logger

Logger.LogInfo("Test")
Logger.LogWarn("Test")
Logger.LogError("Test")
Logger.LogDebug("Test")
Logger.LogDebug("Test, TAG")

def foo():
    try:
        fname = "John"
        lname = "Doe"
        Logger.LogInfo ("Name = {} {}".format(fname, lname))

        x = 0
        Logger.LogDebug("x = {}".format(x))

        y = -1
        Logger.LogWarn("Something may be wrong.")

        raise ValueError('A very specific bad thing happened.')
        
    except Exception as e:
        Logger.LogError("Exception occurred: {}".format(str(e)))

foo()
