import DDPG
import Environnement 
import Runner

Agent = DDPG.DDPGAgent
env_class = Environnement.Environment
agent_class = Agent
batch = 1
verbose = False
ngames = 10000
niter = None

my_runner = Runner.BatchRunner(env_class, agent_class, batch, verbose)
final_reward = my_runner.loop(ngames, niter)