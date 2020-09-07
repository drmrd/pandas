from pathlib import Path
from typing import Optional, Sequence, Union

from pandas.compat._optional import import_optional_dependency

from pandas.core.dtypes.inference import is_list_like

from pandas.core.api import DataFrame


def read_spss(
    path: Union[str, Path],
    usecols: Optional[Sequence[str]] = None,
    convert_categoricals: bool = True,
    encoding: str = None,
) -> DataFrame:
    """
    Load an SPSS file from the file path, returning a DataFrame.

    .. versionadded:: 0.25.0

    Parameters
    ----------
    path : str or Path
        File path.
    usecols : list-like, optional
        Return a subset of the columns. If None, return all columns.
    convert_categoricals : bool, default is True
        Convert categorical columns into pd.Categorical.
    encoding : str, optional
        Encoding of the file at `path`. Must be recognizable by
        `pyreadstat`. If None, attempt to automatically detect the
        encoding.

    Returns
    -------
    DataFrame
    """
    pyreadstat = import_optional_dependency("pyreadstat")

    if usecols is not None:
        if not is_list_like(usecols):
            raise TypeError("usecols must be list-like.")
        else:
            usecols = list(usecols)  # pyreadstat requires a list

    df, _ = pyreadstat.read_sav(
        path,
        usecols=usecols,
        apply_value_formats=convert_categoricals,
        encoding=encoding,
    )
    return df
