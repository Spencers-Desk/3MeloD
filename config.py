# Module where the config classes are made
import os
import tomllib

class MeloDConfig:
    _config_data: dict or None = None

    def __init__(self):
        _config_data = {}
        return

    def could_load_file(self, filepath: str) -> bool:
        """
        Tries to load the config file (provided by the passed filepath). It will return a boolean that
        signals if it loaded successfully (True) or if an error occurred while trying to load it (False).
        :param filepath: A string containing the path to the config file to read from.
        :return: A boolean value that signals if the configuration data loaded successfully or not.
        """
        # First check if the filepath is provided
        if filepath is None or filepath == "":
            print("A config filepath is required in order to load its information.")
            return False

        # Tries to open the file, and parses its data
        try:
            full_path = os.path.abspath(filepath)
            with open(full_path, "rb") as config_file:
                self._config_data = tomllib.load(config_file)
            return True

        # Handles both the known and the "unpredicted" errors
        except tomllib.TOMLDecodeError:
            print("The config file could not be loaded due to a format  error.\n\tCheck the file format and try again.")
            return False
        except FileNotFoundError:
            print("The config file could not be found.")
            return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

    def _get_data_value(self, data_path: str, sep = "/"):
        # Checks if a data_path was provided, or if the iterable list has at least one element to operate with
        data_path_array = data_path.split(sep)
        if data_path is None or data_path == []:
            raise NotValidConfigDataPathException()

        # Iterates over the path data
        data = self._config_data
        for path in data_path_array:
            data = data.get(path)

            # If it finds a non-existent path in any part of the iteration, it throws an error
            if data is None:
                raise NotExistsInConfigException(data_path)

        return data

## Some custom errors to ease the understanding and debugging

class ProjectConfig(MeloDConfig):
    """
    Config class used to load the project configuration data, stored in its appropriate configuration file.
    """

    def __init__(self):
        super().__init__()

    def get_printer_angles_per_step(self) -> (float, float, float):
        """
        Get the printers' angles per step, defined in the project config file.
        :return: the corresponding x-axis, the y-axis, and the z-axis values, in that order.
        """
        return self._get_data_value("printer/x_ang"), \
               self._get_data_value("printer/y_ang"),  \
               self._get_data_value("printer/z_ang")

    def get_printer_rot_distance_per_rev(self) -> (float, float, float):
        """
        Get the printers' rotation distance per revolution (mm), defined in the project config file.
        :return: the corresponding x-axis, the y-axis and the z-axis values, in that order.
        """
        return self._get_data_value("printer/x_rpr"), \
               self._get_data_value("printer/y_rpr"), \
               self._get_data_value("printer/z_rpr")

    def get_printer_dimensions(self) -> (float, float, float):
        """
       Get the printers' dimensions, defined in the project config file.
       :return: the corresponding x-axis, the y-axis and the z-axis values, in that order.
       """
        return self._get_data_value("printer/x_dim"), \
            self._get_data_value("printer/y_dim"), \
            self._get_data_value("printer/z_dim")

    def get_song_config_path(self) -> str:
        return self._get_data_value("song/config_filepath")


class SongConfig(MeloDConfig):
    def __init__(self):
        super().__init__()

    def get_song_properties(self) -> (str, str):
        """
        Get the song properties, defined in the specific song config file.
        :return: the song name and the song directory values, in that order.
        """
        return self._get_data_value("song_name"), \
               self._get_data_value("song_directory")

    def get_song_tempo(self) -> int or float:
        """
          Get the song tempo, defined in the specific song config file.
        :return: the song tempo value.
        """
        return self._get_data_value("tempo")

    def get_song_octaves_adjustment(self) -> (int, int, int):
        return self._get_data_value("x_octave_adj"), \
               self._get_data_value("y_octave_adj"), \
               self._get_data_value("z_octave_adj")



## Error Classes

# Error when the provided datapath is not valid to operate with
class NotValidConfigDataPathException(Exception):
    def __init__(self):
        super().__init__("The data path for the loaded config is not valid.")

# Error when the search of a value inside the dictionary gets to a dead-end
class NotExistsInConfigException(Exception):
    def __init__(self, data_path: str):
        super().__init__(f"The config value searched at {data_path} does not exist.")