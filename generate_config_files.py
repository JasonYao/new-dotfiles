import configparser


class Config:
    def __init__(self, file_name):
        self.parser = configparser.ConfigParser()
        self.add_sections()
        self.file_name = file_name

    def add_sections(self):
        """
        Enables a dynamic dispatch, calling all methods of the calling
        class that has method names beginning with the prefix "add_section".
        """
        sections_to_add = self.get_add_section_names()
        for method_name in sections_to_add:
            getattr(self, method_name)()

    def get_add_section_names(self):
        return sorted([method_name for method_name in dir(self) if callable(getattr(self, method_name)) and method_name.startswith('add_section') and 'add_sections' != method_name])

    def write(self):
        with open(self.file_name, 'w') as config_file:
            self.parser.write(config_file)

    def read(self):
        # TODO P0: Implement w/ correct serializing
        pass


class GeneralConfig(Config):
    def __init__(self):
        super().__init__('general.ini')


class EditorConfig(Config):
    def __init__(self):
        super().__init__('editors.ini')

    def add_section_nano(self):
        nano_language_highlighting = [
            'html', 'css', 'javascript', 'json', 'asm', 'c', 'cmake',
            'sh', 'nanorc', 'java', 'python', 'tex', 'go', 'ruby'
        ]

        self.parser['nano'] = {
            'tab size': '4',
            'show line numbers': True,
            'syntax highlighting': ', '.join(nano_language_highlighting)
        }

    def add_section_vim(self):
        self.parser['vim'] = {
            'show line numbers': True,
            'enable vi emulation': False,
            'enable syntax highlighting': True,
            'colorscheme': 'delek',
            'enable automatic indentation': True,
            'tab width': '4',
            'show matching braces': True,
            'enable spell checking': True,
            'spellchecker': 'en_us',
            'enable misspell underlining': True,
            'dictionary file': 'http://ftp.vim.org/vim/runtime/spell',
            'enable trailing whitespace hightlighting': True,
            'enable incremental search': True
        }


def main():
    general_config = GeneralConfig()
    general_config.write()

    editor_config = EditorConfig()
    editor_config.write()


if __name__ == '__main__':
    main()
