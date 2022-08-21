import hydra
from omegaconf import DictConfig, OmegaConf
import logging
import git


def lam(x, multiplier):
    return x ** multiplier

def log_git_hash()-> str:
	g = git.Git('./')
	hash = g.log().split('\n')[0].split(' ')[1]
	log = logging.getLogger(__name__)
	log.info(hash)
	return hash


@hydra.main(version_base=None, config_path="config", config_name="cfg")
def main(cfg: DictConfig) -> None:
    log = logging.getLogger(__name__)
    log.info(cfg.host_name)
    log_git_hash()
    # for x in range(10):
    #     logger.info(lam(x))

if __name__ == '__main__':
    main()
    

    