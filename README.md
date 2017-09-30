# DressRecommendation

## Creating an environment from an environment.yml file
Create the environment from the environment.yml file:
```
conda env create -f environment.yml
Activate the new environment:
```
- Windows: activate myenv
- macOS and Linux: source activate myenv
- NOTE: Replace myenv with the name of the environment.
- Verify that the new environment was installed correctly:
```
conda list
```

## Activating an environment
To activate an environment:

Windows: ```activate myenv```

macOS and Linux: ```source activate myenv```

Conda prepends the path name myenv onto your system command.

## Deactivating an environment
To deactivate an environment:

Windows: ```deactivate```

macOS and Linux: ```source deactivate```

Conda removes the path name myenv from your system command.

TIP: In Windows, it is good practice to deactivate one environment before activating another.

