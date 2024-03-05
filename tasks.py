from invoke import Context, task

# TODO: hmm what goes here?
# could use this for running local tailwind server


@task
def hey(c: Context) -> None:
    c.run("echo hello world!")
