import hydra
from omegaconf import DictConfig, OmegaConf
import logging


def lam(x, multiplier):
    return x ** multiplier


@hydra.main(version_base=None, config_path="config", config_name="cfg")
def main(cfg: DictConfig) -> None:
    log = logging.getLogger(__name__)
    log.info(cfg.host_name)
    # for x in range(10):
    #     logger.info(lam(x))

if __name__ == '__main__':
    main()
    

    