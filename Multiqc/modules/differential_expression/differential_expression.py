from multiqc.modules.base_module import BaseMultiqcModule
import json

class MultiqcModule(BaseMultiqcModule):
    def __init__(self):
        # Initialise the parent object
        super(MultiqcModule, self).__init__(name='Differential Gene Expression', anchor='dge_module',
        href="",
        info="")
        self.mod_data = dict()
        ###example of finding files specified in the search_patterns.yaml file
        for f in self.find_log_files('differential_expression/json'): 
            path_file = f['fn']

        path_json = None
        with open(path_file,"r") as pf:
            path_json = json.load(pf) 
        
        if path_json:
            img_list = []
            heatmap_file = path_json["heatmap"]
            volcano_file = path_json["volcano"]
            with open(heatmap_file,"r" )as h:
                img_list.append(h.read())
            with open(volcano_file,"r") as r:
                img_list.append(r.read())
            img_html = "\n".join(img_list)
            self.add_section(content=img_html)

        ###add section text content
        self.add_section(
            content = '<p>Insert report section</p>'
        )


