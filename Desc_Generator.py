from HTML_Generator import HTML_Generator
class Description_Generator(HTML_Generator):
    def __init__(self,description_data: dict):
        self.description_data=description_data
        self.description_div_list=[]

    def make_description_div(self):
        '''
        description data form : {'description': 'Auto Teaching Job', 'version': 'v1.0', 'developer': 'Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697'}
        :param description_data: Not Raw Data, only processed data
        :return: html div part for description (list)
        '''

        base_html_head = ['\t\t<div class="description">\n']
        base_html_tail = ['\t\t</div> <!--description END-->  \n\n']
        body_html = []

        if "description" in self.description_data:
            description = self.description_data['description']
            description_html = [
                '\t\t\t<div class="description__description">\n',
                '\t\t\t\t<span class="description__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> <strong>Description</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="description__value">\n',
                '\t\t\t\t' + description + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n'
            ]
            body_html += description_html

        if 'version' in self.description_data:
            version = self.description_data['version']
            version_html = [
                '\t\t\t<div class="description__version">\n',
                '\t\t\t\t<span class="version__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> <strong>Version</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="version__value">\n',
                '\t\t\t\t' + version + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += version_html

        if 'revdate' in self.description_data:
            revdate = self.description_data['revdate']
            revdate_html = [
                '\t\t\t<div class="description__revdate">\n',
                '\t\t\t\t<span class="revdate__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> <strong>Revision Date</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="revdate__value">\n',
                '\t\t\t\t' + revdate + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += revdate_html

        if ('name' in self.description_data) or ('email' in self.description_data) or ('phone' in self.description_data):
            developer_html = [
                '\t\t\t<div class="description__name">\n',
                '\t\t\t\t<span class="name__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> <strong>Developer</strong> \n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += developer_html

        if 'name' in self.description_data:
            name = self.description_data['name']
            name_html = [
                '\t\t\t<div class="description__name">\n',
                '\t\t\t\t<span class="name__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> <strong>name</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="name__value">\n',
                '\t\t\t\t' + name + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += name_html

        if 'email' in self.description_data:
            email = self.description_data['email']
            email_html = [
                '\t\t\t<div class="description__email">\n',
                '\t\t\t\t<span class="email__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> <strong>email</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="email__value">\n',
                '\t\t\t\t' + email + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += email_html

        if 'phone' in self.description_data:
            phone = self.description_data['phone']
            phone_html = [
                '\t\t\t<div class="description_phone">\n',
                '\t\t\t\t<span class="phone__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> <strong>phone</strong> : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="phone__value">\n',
                '\t\t\t\t' + phone + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>  <!--class="description_phone END-->\n\n',
            ]
            body_html += phone_html

        if 'readme' in self.description_data:

            readme = self.description_data['readme']
            readme_html_head = ['\t\t\t<div class="description_readme">\n'
                                '\t\t\t\t<span class="readme__title">\n',
                                '\t\t\t\t<i class="fas fa-square"></i> <strong>Notice</strong> : \n',
                                '\t\t\t\t<br></span>\n',
                                ]
            readme_html_tail = ['\t\t\t</div>\n\n']
            readme_html_body = []
            for idx, line in enumerate(readme):
                class_name = "readme_" + str(idx)
                html_line = ['\t\t\t\t<span class="' + class_name + '">\n',
                             '\t\t\t\t\t' + line + '\n',
                             '\t\t\t\t<br></span>\n']

                readme_html_body += html_line

            body_html += (readme_html_head + readme_html_body + readme_html_tail)

        self.description_div_list = base_html_head + body_html + base_html_tail

    def return_description_div(self):
        self.make_description_div()
        return self.description_div_list