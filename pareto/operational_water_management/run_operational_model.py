##############################################################################
#
##############################################################################
from pareto.operational_water_management.operational_produced_water_optimization_model import (
    create_model,
    ProdTank,
)
from pareto.utilities.get_data import get_data
from pareto.utilities.results import generate_report, PrintValues
from importlib import resources
from pyomo.environ import SolverFactory

import pandas as pd

# This emulates what the pyomo command-line tools does
# Tabs in the input Excel spreadsheet
set_list = [
    "ProductionPads",
    "CompletionsPads",
    "ProductionTanks",
    "FreshwaterSources",
    "StorageSites",
    "SWDSites",
    "TreatmentSites",
    "ReuseOptions",
    "NetworkNodes",
]
parameter_list = [
    "FCA",
    "PCT",
    "FCT",
    "CCT",
    "PKT",
    "PRT",
    "CKT",
    "CRT",
    "PAL",
    "CompletionsDemand",
    "PadRates",
    "FlowbackRates",
    "ProductionTankCapacity",
    "InitialDisposalCapacity",
    "CompletionsPadStorage",
    "TreatmentCapacity",
    "FreshwaterSourcingAvailability",
    "PadOffloadingCapacity",
    "DriveTimes",
    "DisposalPipeCapEx",
    "DisposalOperationalCost",
    "TreatmentOperationalCost",
    "ReuseOperationalCost",
    "PipingOperationalCost",
    "TruckingHourlyCost",
    "FreshSourcingCost",
    "ProductionRates",
]

# user needs to provide the path to the case study data file
# for example: 'C:\\user\\Documents\\myfile.xlsx'
# note the double backslashes '\\' in that path reference
fname = "case_studies\\EXAMPLE_INPUT_DATA_FILE_generic_operational_model.xlsx"
[df_sets, df_parameters] = get_data(fname, set_list, parameter_list)

df_parameters["MinTruckFlow"] = 75
df_parameters["MaxTruckFlow"] = 37000
# create mathematical model
operational_model = create_model(
    df_sets,
    df_parameters,
    default={"has_pipeline_constraints": True, "production_tanks": ProdTank.individual},
)

# import pyomo solver
opt = SolverFactory("cbc")
opt.options["seconds"] = 60
# solve mathematical model
results = opt.solve(operational_model, tee=True)
results.write()
print("\nDisplaying Solution\n" + "-" * 60)
# pyomo_postprocess(None, model, results)
# print results
[model, results_dict] = generate_report(
    operational_model, is_print=[PrintValues.Detailed]
)
fname = "generic_operational_optimization_results.xlsx"
with pd.ExcelWriter(fname) as writer:
    for i in results_dict:
        df = pd.DataFrame(results_dict[i][1:], columns=results_dict[i][0])
        df.to_excel(writer, sheet_name=i)
