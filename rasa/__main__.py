import argparse
import logging
import os
import platform  # 导入标准库 `platform`，此库可提供访问平台标识数据的功能，例如操作系统、平台版本等。
import sys  # 导入 `sys` 模块，它提供对一些 Python 解释器使用或维护的变量和函数的访问。

from rasa_sdk import __version__ as rasa_sdk_version  # 从 `rasa_sdk` 模块中导入 `__version__` 并将其别名设置为 `rasa_sdk_version`。`__version__` 通常用于表示模块的版本号。
from rasa.constants import MINIMUM_COMPATIBLE_VERSION  # 从 `rasa.constants` 模块中导入 `MINIMUM_COMPATIBLE_VERSION`，它代表 Rasa 框架的最低兼容版本。
from rasa.utils.log_utils import configure_structlog  # 从 `rasa.utils.log_utils` 模块中导入 `configure_structlog` 函数，该函数用于配置 structlog 库，使其适用于 Rasa 的日志记录需求。

import rasa.telemetry  # 导入 `rasa.telemetry` 模块，它可能用于收集和发送使用 Rasa 的遥测数据。
import rasa.utils.io  # 导入 `rasa.utils.io` 模块，它可能包含有关 IO 操作的各种实用函数。
import rasa.utils.tensorflow.environment as tf_env  # 从 `rasa.utils.tensorflow.environment` 模块中导入所有内容，并将其别名设置为 `tf_env`，此模块可能包含有关 TensorFlow 环境配置的函数。
from rasa import version  # 从 `rasa` 包中导入 `version`，它可能表示 Rasa 的版本号。
from rasa.cli import (  # 从 `rasa.cli` 模块中导入多个子模块，如 `data`, `export`, `interactive`, `run`, `scaffold`, `shell`, `telemetry`, `test`, `train`, `visualize`, `x`, `evaluate`。这些子模块提供了各种 CLI（命令行界面）功能。
    data,
    export,
    interactive,
    run,
    scaffold,
    shell,
    telemetry,
    test,
    train,
    visualize,
    x,
    evaluate,
)
from rasa.cli.arguments.default_arguments import add_logging_options  # 从 `rasa.cli.arguments.default_arguments` 模块中导入 `add_logging_options` 函数，此函数可能用于添加日志记录选项。
from rasa.cli.utils import parse_last_positional_argument_as_model_path  # 从 `rasa.cli.utils` 模块中导入 `parse_last_positional_argument_as_model_path` 函数，该函数可能用于解析作为模型路径的命令行参数。
from rasa.plugin import plugin_manager  # 从 `rasa.plugin` 模块中导入 `plugin_manager`，它可能是用于管理 Rasa 插件的对象或者函数。
from rasa.shared.exceptions import RasaException  # 从 `rasa.shared.exceptions` 模块中导入 `RasaException`，这是 Rasa 所有自定义异常的基类。
from rasa.shared.utils.cli import print_error  # 从 `rasa.shared.utils.cli` 模块中导入 `print_error` 函数，此函数可能用于打印错误信息。
from rasa.utils.common import configure_logging_and_warnings  # 从 `rasa.utils.common` 模块中导入 `configure_logging_and_warnings` 函数，此函数可能用于配置日志记录和警告。

logger = logging.getLogger(__name__)  # 创建一个名为 `__name__` 的日志记录器对象，它可以用于在此模块中记录日志。`__name__` 是一个内置变量，代表当前模块的名字。



def create_argument_parser() -> argparse.ArgumentParser:
    """Parse all the command line arguments for the training script."""
    parser = argparse.ArgumentParser(
        prog="rasa",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Rasa command line interface. Rasa allows you to build "
        "your own conversational assistants 🤖. The 'rasa' command "
        "allows you to easily run most common commands like "
        "creating a new bot, training or evaluating models.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Print installed Rasa version",
    )

    parent_parser = argparse.ArgumentParser(add_help=False)
    add_logging_options(parent_parser)
    parent_parsers = [parent_parser]

    subparsers = parser.add_subparsers(help="Rasa commands")

    scaffold.add_subparser(subparsers, parents=parent_parsers)
    run.add_subparser(subparsers, parents=parent_parsers)
    shell.add_subparser(subparsers, parents=parent_parsers)
    train.add_subparser(subparsers, parents=parent_parsers)
    interactive.add_subparser(subparsers, parents=parent_parsers)
    telemetry.add_subparser(subparsers, parents=parent_parsers)
    test.add_subparser(subparsers, parents=parent_parsers)
    visualize.add_subparser(subparsers, parents=parent_parsers)
    data.add_subparser(subparsers, parents=parent_parsers)
    export.add_subparser(subparsers, parents=parent_parsers)
    x.add_subparser(subparsers, parents=parent_parsers)
    evaluate.add_subparser(subparsers, parents=parent_parsers)
    plugin_manager().hook.refine_cli(
        subparsers=subparsers, parent_parsers=parent_parsers
    )

    return parser


def print_version() -> None:
    """Prints version information of rasa tooling and python."""
    print(f"Rasa Version      :         {version.__version__}")
    print(f"Minimum Compatible Version: {MINIMUM_COMPATIBLE_VERSION}")
    print(f"Rasa SDK Version  :         {rasa_sdk_version}")
    print(f"Python Version    :         {platform.python_version()}")
    print(f"Operating System  :         {platform.platform()}")
    print(f"Python Path       :         {sys.executable}")

    result = plugin_manager().hook.get_version_info()
    if result:
        print(f"\t{result[0][0]}  :         {result[0][1]}")


def main() -> None:
    """Run as standalone python application."""
    parse_last_positional_argument_as_model_path()
    arg_parser = create_argument_parser()
    cmdline_arguments = arg_parser.parse_args()

    log_level = getattr(cmdline_arguments, "loglevel", None)
    logging_config_file = getattr(cmdline_arguments, "logging_config_file", None)
    configure_logging_and_warnings(
        log_level, logging_config_file, warn_only_once=True, filter_repeated_logs=True
    )

    tf_env.setup_tf_environment()
    tf_env.check_deterministic_ops()

    # insert current path in syspath so custom modules are found
    sys.path.insert(1, os.getcwd())

    try:
        if hasattr(cmdline_arguments, "func"):
            rasa.utils.io.configure_colored_logging(log_level)

            result = plugin_manager().hook.configure_commandline(
                cmdline_arguments=cmdline_arguments
            )
            endpoints_file = result[0] if result else None

            rasa.telemetry.initialize_telemetry()
            rasa.telemetry.initialize_error_reporting()
            plugin_manager().hook.init_telemetry(endpoints_file=endpoints_file)
            plugin_manager().hook.init_managers(endpoints_file=endpoints_file)
            plugin_manager().hook.init_anonymization_pipeline(
                endpoints_file=endpoints_file
            )
            # configure structlog
            configure_structlog(log_level)

            cmdline_arguments.func(cmdline_arguments)
        elif hasattr(cmdline_arguments, "version"):
            print_version()
        else:
            # user has not provided a subcommand, let's print the help
            logger.error("No command specified.")
            arg_parser.print_help()
            sys.exit(1)
    except RasaException as e:
        # these are exceptions we expect to happen (e.g. invalid training data format)
        # it doesn't make sense to print a stacktrace for these if we are not in
        # debug mode
        logger.debug("Failed to run CLI command due to an exception.", exc_info=e)
        print_error(f"{e.__class__.__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
