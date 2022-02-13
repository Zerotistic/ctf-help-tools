def main(argv):
  path_to_binary = argv[1]
  project = angr.Project(path_to_binary)
  initial_state = project.factory.entry_state()
  simulation = project.factory.simgr(initial_state)

  def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())

    return 'Good Job' in str(stdout_output) # :boolean

  def should_abort(state): 
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    
    return 'Try again' in str(stdout_output)  # :boolean

  simulation.explore(find=is_successful, avoid=should_abort)
