## Installer un éditeur de texte digne de ce nom (atom ou notepad++)
S'assurer qu'il n'y a pas de Tabs mais des espaces

## Installer GitHub Desktop
Cloner https://github.com/oliche/jwaclassic
Se mettre sur la branche develop

## Installer Linux Subsystem for Windows

Activer Linux subsystem for Windows: dans Power shell (en tant qu' administrateur)

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Telecharger l'app WIndows Ubuntu par le Microsoft Store, installer et lancer
ou dans Powershell en tant qu'administrateur, écrire la commande suivante :

    lxrun /install

## Dans l'invite de commande Ubuntu, installer Jekyll

    sudo apt-get update
    sudo apt-get install ruby-full build-essential zlib1g-dev
Installer Ruby

    echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
Configurer l'emplacement des Gems

    sudo gem install jekyll bundler
Installer une nouvelle Gem


## Lancer le site: dans une invite Ubuntu

    GIT_FOLDER=/mnt/c/Users/Joël/Documents/GitHub/jwaclassic
    DROPBOX_IMAGES=/mnt/d/Dropbox/#_Site_internet_JWA/Images
    rsync -av --progress  $DROPBOX_IMAGES/* $GIT_FOLDER/images/
    cd $GIT_FOLDER
    bundle exec jekyll serve --config _config.yml,_config_dev.yml --destination ./_site

Eventuellement créer un script nommé jwaclassic dans home contenant les lignes ci-dessud et taper
    ./jwaclassic

Taper dans un navigateur web:
    http://localhost:4000
