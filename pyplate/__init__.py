from pathlib import Path
import os
import yaml

# import pyplate


class Config:
    def __init__(self):
        file_path = None
        for path in [Path(os.environ.get('PYPLATE_CONFIG', '')), Path.home(), Path(os.path.dirname(__file__))]:
            path = path.joinpath('pyplate.yaml')
            if path.is_file():
                file_path = path
                break

        if file_path is None:
            raise RuntimeError("pyplate.yaml not found.")

        try:
            with file_path.open('r') as config_file:
                yaml_config = yaml.safe_load(config_file)
        except yaml.YAMLError as exc:
            raise RuntimeError("Config file could not be read.") from exc

        self.internal_precision = yaml_config['internal_precision']
        self.moles_storage_unit = yaml_config['moles_storage_unit']
        assert self.moles_storage_unit[-3:] == 'mol'
        self.moles_display_unit = yaml_config['moles_display_unit']
        assert self.moles_display_unit[-3:] == 'mol'
        self.volume_storage_unit = yaml_config['volume_storage_unit']
        assert self.volume_storage_unit[-1] == 'L'
        self.volume_display_unit = yaml_config['volume_display_unit']
        assert self.volume_display_unit[-1] == 'L'

        self.default_solid_density = float(yaml_config['default_solid_density'])
        self.default_enzyme_density = float(yaml_config['default_enzyme_density'])
        self.default_weight_volume_units = yaml_config['default_weight_volume_units']


        self.default_colormap = yaml_config['default_colormap']
        self.default_diverging_colormap = yaml_config['default_diverging_colormap']
        self.precisions = yaml_config['precisions']


from .pyplate import Substance, Container, Plate, Recipe
