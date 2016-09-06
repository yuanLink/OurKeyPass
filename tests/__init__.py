import imp
import pkgutil

def load_tests(loader, suite, pattern):
    for imp, modname, _ in pkgutil.walk_packages(__path__):
        mod = imp.find_module(modname).load_module(modname)
        print(imp)
        print(modname)
        for test in loader.loadTestsFromModule(mod):
            suite.addTests(test)

    return suite
