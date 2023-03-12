from invoke import task

@task
def start(ctx):
    ctx.run("cd dist && ./server")

@task
def test(ctx):
    ctx.run("pytest tests")

@task
def performance(ctx):
    print("Running performance tests for the Trie, this may take up to a minute.")
    ctx.run("python3 performance/performance_trie.py")
    print("Running performance tests for the Markov generator, this may take a couple minutes.")
    ctx.run("python3 performance/performance_markov.py")

@task
def pylint(ctx):
    ctx.run("pylint services/ server.py")