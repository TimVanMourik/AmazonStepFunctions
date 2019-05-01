#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe











#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')
analysisflow.connect(FetchAnOrder, "output", RegionChoice, "input")
analysisflow.connect(RegionChoice, "output", CreateOrderB, "input")
analysisflow.connect(RegionChoice, "output", NoOrderPossible, "input")
analysisflow.connect(RegionChoice, "output", UnservedRegion, "input")
analysisflow.connect(CreateOrderB, "output", DatabaseError, "input")
analysisflow.connect(NoOrderPossible, "output", OrderOK, "input")
analysisflow.connect(CreateOrderB, "output", OrderOK, "input")
analysisflow.connect(DatabaseError, "output", NoOrderPossible_1, "input")
analysisflow.connect(UnservedRegion, "output", NoOrderPossible_1, "input")

#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
