﻿Strategic Water Management
==========================

Overview
--------

Given a set of existing network components (completion pads, storage pads, production pads, and distribution options like trucks and/or pipelines) and capacity expansion options, the strategic water management model provides an insight into financial opportunities and mid-long term investment decisions to reduce operational costs or maximize reuse or reduce fresh water consumption.

+---------------------------------------------------------+
| Section                                                 |
+=========================================================+
| :ref:`strategic_model_terminology`                      |
+---------------------------------------------------------+
| :ref:`strategic_model_mathematical_notation`            |
+---------------------------------------------------------+
| :ref:`strategic_model_mathematical_program_formulation` |
+---------------------------------------------------------+
| :ref:`strategic_model_water_quality_extension`          |
+---------------------------------------------------------+
| :ref:`strategic_model_references`                       |
+---------------------------------------------------------+


.. _strategic_model_terminology:

Terminology
-----------

**Beneficial Reuse Options:** This term refers to the reuse of water at mining facilities, farms, etc.

**Completions Demand:** Demand set by completions pads.  This demand can be met by produced water, treated water, or freshwater.

**Completions Reuse Water:** Water that meets demand at a completions site. This does not include freshwater or water for beneficial reuse.

**Network Nodes:** These are branch points for pipelines only.

.. note:: Well pads are not a subset of network nodesd.

**[t]:** This notation indicates that timing of capacity expansion has not yet been implemented.

**Terminal Storage Level:** These are goal storage levels for the final time period. Without this, the storage levels would likely be depleted in the last time period.

**Water Boosting:** Moving large volumes of water requires water pumps. Water boosting refers to the infrastructure required to maintain water pressure.


.. _strategic_model_mathematical_notation:

Strategic Model Mathematical Notation
-------------------------------------

**Sets**

:math:`\textcolor{blue}{t \in T}`			                               Time periods (i.e. days)

:math:`\textcolor{blue}{p \in P}`			                               Well pads

:math:`\textcolor{blue}{p \in PP}`			                           Production pads (subset of well pads P)

:math:`\textcolor{blue}{p \in CP}`		                               Completions pads (subset of well pads P)

:math:`\textcolor{blue}{f \in F}`			                               Freshwater sources

:math:`\textcolor{blue}{k \in K}`			                               Disposal sites

:math:`\textcolor{blue}{s \in S}`			                               Storage sites

:math:`\textcolor{blue}{r \in R}`			                               Treatment sites

:math:`\textcolor{blue}{o \in O}`			                               Beneficial Reuse options

:math:`\textcolor{blue}{n \in N}`			                               Network nodes

:math:`\textcolor{blue}{l \in L}`			                               Locations (superset of well pads, disposal sites, nodes, ...)

:math:`\textcolor{blue}{d \in D}`			                               Pipeline Diameters

:math:`\textcolor{blue}{c \in C}`				                           Storage capacities

:math:`\textcolor{blue}{j \in J}`				                           Treatment capacities

:math:`\textcolor{blue}{i \in I}`				                           Injection (i.e. disposal) capacities

:math:`\textcolor{blue}{(p,p) \in PCA}`	                               Production-to-completions pipeline arcs

:math:`\textcolor{blue}{(p,n) \in PNA}`                                 Production-to-node pipeline arcs

:math:`\textcolor{blue}{(p,p) \in PPA}`                                 Production-to-production pipeline arcs

:math:`\textcolor{blue}{(p,n) \in CNA}`	                               Completions-to-node pipeline arcs

:math:`\textcolor{blue}{(p,p) \in CCA}`	                               Completions-to-completions pipeline arcs

:math:`\textcolor{blue}{(n,n) \in NNA}`                                 Node-to-node pipeline arcs

:math:`\textcolor{blue}{(n,p) \in NCA}`                                 Node-to-completions pipeline arcs

:math:`\textcolor{blue}{(n,k) \in NKA}`	                               Node-to-disposal pipeline arcs

:math:`\textcolor{blue}{(n,s) \in NSA}`	                               Node-to-storage pipeline arcs

:math:`\textcolor{blue}{(n,r) \in NRA}`                                 Node-to-treatment pipeline arcs

:math:`\textcolor{blue}{(n,o) \in NOA}`	                               Node-to-beneficial reuse pipeline arcs

:math:`\textcolor{blue}{(f,p) \in FCA}`	                               Freshwater-to-completions pipeline arcs

:math:`\textcolor{blue}{(r,n) \in RNA}`	                               Treatment-to-node pipeline arcs

:math:`\textcolor{blue}{(r,p) \in RCA}`	                               Treatment-to-completions pipeline arcs

:math:`\textcolor{blue}{(r,k) \in RKA}`	                               Treatment-to-disposal pipeline arcs

:math:`\textcolor{blue}{(r,s) \in RSA}`			                       Treatment-to-storage pipeline arcs

:math:`\textcolor{blue}{(s,n) \in SNA}`	                               Storage-to-node pipeline arcs

:math:`\textcolor{blue}{(s,p) \in SCA}`	                               Storage-to-completions pipeline arcs

:math:`\textcolor{blue}{(s,k) \in SKA}`	                               Storage-to-disposal pipeline arcs

:math:`\textcolor{blue}{(s,r) \in SRA}`	                               Storage-to-treatment pipeline arcs

:math:`\textcolor{blue}{(s,o) \in SOA}`	                               Storage-to-beneficial reuse pipeline arcs

:math:`\textcolor{blue}{(p,p) \in PCT}`	                               Production-to-completions trucking arcs

:math:`\textcolor{blue}{(p,k) \in PKT}`	                               Production-to-disposal trucking arcs

:math:`\textcolor{blue}{(p,s) \in PST}`                                 Production-to-storage trucking arcs

:math:`\textcolor{blue}{(p,r) \in PRT}`	                               Production-to-treatment trucking arcs

:math:`\textcolor{blue}{(p,o) \in POT}`	                               Production-to-beneficial reuse trucking arcs

:math:`\textcolor{blue}{(f,c) \in FCT}`                                 Freshwater-to-completions trucking arcs

:math:`\textcolor{blue}{(p,k) \in CKT}`	                               Completions-to-disposal trucking arcs

:math:`\textcolor{blue}{(p,s) \in CST}`	                               Completions-to-storage trucking arcs

:math:`\textcolor{blue}{(p,r) \in CRT}`                                 Completions-to-treatment trucking arcs

:math:`\textcolor{blue}{(p,p) \in CCT}`	                               Completions-to-completions trucking arcs (flowback reuse)

:math:`\textcolor{blue}{(s,p) \in SCT}`                                 Storage-to-completions trucking arcs

:math:`\textcolor{blue}{(s,k) \in SKT}`                                 Storage-to-disposal trucking arcs

:math:`\textcolor{blue}{(r,k) \in RKT}`	                               Treatment-to-disposal trucking arcs


**Continuous Variables**

:math:`\textcolor{red}{F_{l,l,t}^{Piped}}` =                           Produced water piped from one location to another location

:math:`\textcolor{red}{F_{l,l,t}^{Trucked}}` =	                       Water trucked from one location to another location

:math:`\textcolor{red}{F_{f,p,t}^{Sourced}}` =                         Fresh water sourced from source to completions

:math:`\textcolor{red}{F_{p,t}^{PadStorageIn}}` =	                   Water put into completions pad storage

:math:`\textcolor{red}{F_{p,t}^{PadStorageOut}}` =	                   Water removed from completions pad storage

:math:`\textcolor{red}{F_{r,t}^{TreatmentDestination}}` =	           Water delivered to treatment site

:math:`\textcolor{red}{F_{r,t}^{UnusedTreatedWater}}` =	               Treated water that is not used

:math:`\textcolor{red}{F_{k,t}^{DisposalDestination}}` =               Water injected at disposal site

:math:`\textcolor{red}{F_{p,t}^{CompletionsReuseDestination}}` =	   Water delivered to completions pad for reuse

:math:`\textcolor{red}{F_{p,t}^{CompletionsDestination}}` =	           All water delivered to completions pad

:math:`\textcolor{red}{F_{p,t}^{BeneficialReuseDestination}}` =	       Water delivered to beneficial reuse site

:math:`\textcolor{red}{L_{s,t}^{Storage}}` =	                       Water level at storage site at the end of time period t

:math:`\textcolor{red}{L_{p,t}^{PadStorage}}` =	                       Water level in completions pad storage  at the end of time period t

:math:`\textcolor{red}{F^{TotalTrucked}}` =	                           Total volume of water trucked

:math:`\textcolor{red}{F^{TotalSourced}}` =                            Total volume of freshwater sourced

:math:`\textcolor{red}{F^{TotalDisposed}}` =                           Total volume of produced water disposed

:math:`\textcolor{red}{F^{TotalCompletionsReuse}}` =                   Total volume of produced water reused

:math:`\textcolor{red}{C_{l,l,t}^{Piped}}` =	                       Cost of piping produced water from one location to another location

:math:`\textcolor{red}{C_{l,l,t}^{Trucked}}` =	                       Cost of trucking produced water from one location to another location

:math:`\textcolor{red}{C_{f,p,t}^{Sourced}}` =	                       Cost of sourcing fresh water from source to completions pad

:math:`\textcolor{red}{C_{k,t}^{Disposal}}` =                          Cost of injecting produced water at disposal site

:math:`\textcolor{red}{C_{r,t}^{Treatment}}` =	                       Cost of treating produced water at treatment site

:math:`\textcolor{red}{C_{p,t}^{CompletionsReuse}}` =                  Cost of reusing produced water at completions site

:math:`\textcolor{red}{C_{s,t}^{Storage}}` =                           Cost of storing produced water at storage site (incl. treatment)

:math:`\textcolor{red}{R_{s,t}^{Storage}}` =                           Credit for retrieving stored produced water from storage site

:math:`\textcolor{red}{C^{TotalSourced}}` =                            Total cost of sourcing freshwater

:math:`\textcolor{red}{C^{TotalDisposal}}` =                           Total cost of injecting produced water

:math:`\textcolor{red}{C^{TotalTreatment}}` = 	                       Total cost of treating produced water

:math:`\textcolor{red}{C^{TotalCompletionsReuse}}` =                   Total cost of reusing produced water

:math:`\textcolor{red}{C^{TotalPiping}}` = 	                           Total cost of piping produced water

:math:`\textcolor{red}{C^{TotalStorage}}` =                            Total cost of storing produced water

:math:`\textcolor{red}{C^{TotalTrucking}}` =                           Total cost of trucking produced water

:math:`\textcolor{red}{C^{Slack}}` =                                   Total cost of slack variables

:math:`\textcolor{red}{R^{TotalStorage}}` = 	                       Total credit for withdrawing produced water

:math:`\textcolor{red}{D_{k,[t]}^{Capacity}}` =                        Disposal capacity in a given time period at disposal site

:math:`\textcolor{red}{X_{s,[t]}^{Capacity}}` =                        Storage capacity in a given time period at storage site

:math:`\textcolor{red}{T_{r,[t]}^{Capacity}}` =                        Treatment capacity in a given time period at treatment site

:math:`\textcolor{red}{F_{l,l,[t]}^{Capacity}}` =                      Flow capacity in a given time period between two locations

:math:`\textcolor{red}{C_{[t]}^{DisposalCapEx}}` =                     Capital cost of constructing or expanding disposal capacity

:math:`\textcolor{red}{C_{[t]}^{PipelineCapEx}}` =                     Capital cost of constructing or expanding piping capacity

:math:`\textcolor{red}{C_{[t]}^{StorageCapEx}}` =                      Capital cost of constructing or expanding storage capacity

:math:`\textcolor{red}{C_{[t]}^{TreatmentCapEx}}` =                    Capital cost of constructing or expanding treatment capacity

:math:`\textcolor{red}{S_{p,t}^{FracDemand}}` =  	                   Slack variable to meet the completions water demand

:math:`\textcolor{red}{S_{p,t}^{Production}}` = 	                   Slack variable to process produced water production

:math:`\textcolor{red}{S_{p,t}^{Flowback}}` = 	                       Slack variable to process flowback water production

:math:`\textcolor{red}{S_{l,l}^{Pipeline Capacity}}` =                 Slack variable to provide necessary pipeline capacity

:math:`\textcolor{red}{S_{s}^{StorageCapacity}}` =                     Slack variable to provide necessary storage capacity

:math:`\textcolor{red}{S_{k}^{DisposalCapacity}}` =                    Slack variable to provide necessary disposal capacity

:math:`\textcolor{red}{S_{r}^{TreamentCapacity}}` =                    Slack variable to provide necessary treatment capacity

:math:`\textcolor{red}{S_{o}^{BeneficialResueCapacity}}` =             Slack variable to provide necessary beneficial reuse capacity


**Binary Variables**

:math:`\textcolor{red}{y_{l,l,d}^{Pipeline}}` =                        New pipeline installed between one location and another location with specific diameter

:math:`\textcolor{red}{y_{s,c}^{Storage}}` =                           New or additional storage facility installed at storage site with specific storage capacity

:math:`\textcolor{red}{y_{r,j}^{Treatment}}` =                         New or additional treatment facility installed at treatment site with specific treatment capacity

:math:`\textcolor{red}{y_{k,i}^{Disposal}}` =                          New or additional disposal facility installed at disposal site with specific injection capacity

:math:`\textcolor{red}{y_{l,l,t}^{Flow}}` =                            Directional flow between two locations

..
    :math:`\textcolor{red}{z_{l,l,d,t}^{Pipeline}}` =                      Timing of pipeline installation between one location and another location with specific diameter

    :math:`\textcolor{red}{z_{s,c,t}^{Storage}}` =                         Timing of storage facility installation at storage site with specific storage capacity

    :math:`\textcolor{red}{z_{k,i,t}^{Disposal}}` =                        Timing of disposal facility installation at disposal site with specific injection capacity


**Parameters**

:math:`\textcolor{green}{\gamma_{p,t}^{Completions}}` = 	                   Completions demand at a completions site in a time period

:math:`\textcolor{green}{\gamma^{TotalDemand}}` =                           Total water demand over the planning horizon

:math:`\textcolor{green}{\beta_{p,t}^{Production}}` = 	                   Produced water supply forecast for a production pad

:math:`\textcolor{green}{\beta_{p,t}^{Flowback}}` =	                       Flowback supply forecast for a completions pad

:math:`\textcolor{green}{\beta^{TotalProd}}` =                             Total water production (production & flowback) over the planning horizon

:math:`\textcolor{green}{\sigma_{l,l}^{Pipeline}}` =	                       Initial pipeline capacity between two locations

:math:`\textcolor{green}{\sigma_{k}^{Disposal}}` =	                       Initial disposal capacity at a disposal site

:math:`\textcolor{green}{\sigma_{s}^{Storage}}` =                           Initial storage capacity at a storage site

:math:`\textcolor{green}{\sigma_{p,t}^{PadStorage}}` =                      Storage capacity at completions site

:math:`\textcolor{green}{\sigma_{r}^{Treatment}}` =                         Initial treatment capacity at a treatment site

:math:`\textcolor{green}{\sigma_{o}^{BeneficialReuse}}` =                   Initial reuse capacity at a reuse site

:math:`\textcolor{green}{\sigma_{f,t}^{Freshwater}}` =                      Freshwater sourcing capacity at freshwater source

:math:`\textcolor{green}{\sigma_{p}^{Offloading,Pad}}` =                    Truck offloading sourcing capacity per pad

:math:`\textcolor{green}{\sigma_{s}^{Offloading,Storage}}` =	               Truck offloading sourcing capacity per storage site

:math:`\textcolor{green}{\sigma_{p}^{Processing,Pad}}` =                    Processing (e.g. clarification) capacity per pad

:math:`\textcolor{green}{\sigma_{s}^{Processing,Storage}}` =                Processing (e.g. clarification) capacity at storage site

:math:`\textcolor{green}{\sigma_{n}^{Node}}` =                              Capacity per network node

:math:`\textcolor{green}{W_{r}^{TreatmentComponent}}` =                Water quality component treated for at treatment site

:math:`\textcolor{green}{\epsilon_{r, w}^{Treatment}}` =                      Treatment efficiency at treatment site

:math:`\textcolor{green}{\alpha^{AnnualizationRate}}` =                     Annualization Rate [%]

:math:`\textcolor{green}{\delta_{i}^{Disposal}}` =                          Increments for installation/expansion of disposal capacity

:math:`\textcolor{green}{\delta_{c}^{Storage}}` =                           Increments for installation/expansion of storage capacity

:math:`\textcolor{green}{\delta_{j}^{Treatment}}` =                         Increments for installation/expansion of treatment capacity

:math:`\textcolor{green}{\delta^{Truck}}` =                                 Truck capacity

:math:`\textcolor{green}{\tau_{k}^{Disposal}}` =                          Disposal construction or expansion lead time

:math:`\textcolor{green}{\tau_{s}^{Storage}}` =                           Storage construction or expansion lead time

:math:`\textcolor{green}{\tau_{l,l}^{Pipeline}}` =                        Pipeline construction or expansion lead time

:math:`\textcolor{green}{\tau_{p,p}^{Trucking}}` =                        Drive time between two pads

:math:`\textcolor{green}{\tau_{p,k}^{Trucking}}` =	                       Drive time from a pad to a disposal site

:math:`\textcolor{green}{\tau_{p,s}^{Trucking}}` =	                       Drive time from a pad to a storage site

:math:`\textcolor{green}{\tau_{p,r}^{Trucking}}` =	                       Drive time from a pad to a treatment site

:math:`\textcolor{green}{\tau_{p,o}^{Trucking}}` =                        Drive time from a pad to a beneficial reuse site

:math:`\textcolor{green}{\tau_{s,p}^{Trucking}}` =	                       Drive time from a storage site to a completions site

:math:`\textcolor{green}{\tau_{s,k}^{Trucking}}` =                        Drive time from a storage site to a disposal site

:math:`\textcolor{green}{\tau_{r,k}^{Trucking}}` =                        Drive time from a treatment site to a disposal site

:math:`\textcolor{green}{\lambda_{s}^{Storage}}` =                           Initial storage level at storage site

:math:`\textcolor{green}{\lambda_{p}^{PadStorage}}` =                        Initial storage level at completions site

:math:`\textcolor{green}{\theta_{s}^{Storage}}` =                           Terminal storage level at storage site

:math:`\textcolor{green}{\theta_{p}^{PadStorage}}` =                        Terminal storage level at completions site

:math:`\textcolor{green}{\kappa_{k,i}^{Disposal}}` =                        Disposal construction or expansion capital cost for selected capacity increment

:math:`\textcolor{green}{\kappa_{s,c}^{Storage}}` =                         Storage construction or expansion capital cost for selected capacity increment

:math:`\textcolor{green}{\kappa_{r,j}^{Treatment}}` =                       Treatment construction or expansion capital cost for selected capacity increment


**The cost parameter for expanding or constructing new pipeline capacity is structured differently depending on model configuration settings. If the pipeline cost configuration is distance based:**

    :math:`\textcolor{green}{\kappa^{Pipeline}}` =                              Pipeline construction or expansion capital cost [currency/(diameter-distance)]

    :math:`\textcolor{green}{\mu_{d}^{Pipeline}}` =                          Pipeline diameter installation or expansion increments  [diameter]

    :math:`\textcolor{green}{\lambda_{l,l}^{Pipeline}}` = 	                   Pipeline segment length [distance]

**Otherwise, if the pipeline cost configuration is capacity based:**

    :math:`\textcolor{green}{\kappa_{l,l,d}^{Pipeline}}` =                      Pipeline construction or expansion capital cost for selected diameter capacity [currency/(volume/time)]

    :math:`\textcolor{green}{\delta_{d}^{Pipeline}}` =                          Increments for installation/expansion of pipeline capacity [volume/time]


:math:`\textcolor{green}{\pi_{k}^{Disposal}}` =                          Disposal operational cost

:math:`\textcolor{green}{\pi_{r}^{Treatment}}` =	                       Treatment operational cost (may include "clean brine")

:math:`\textcolor{green}{\pi_{p}^{CompletionReuse}}` =                   Completions reuse operational cost

:math:`\textcolor{green}{\pi_{s}^{Storage}}` =                           Storage deposit operational cost

:math:`\textcolor{green}{\rho_{s}^{Storage}}` =                           Storage withdrawal operational credit

:math:`\textcolor{green}{\pi_{l,l}^{Pipeline}}` =	                       Pipeline operational cost

:math:`\textcolor{green}{\pi_{l}^{Trucking}}` =                          Trucking hourly cost (by source)

:math:`\textcolor{green}{\pi_{f}^{Sourcing}}` =                          Fresh sourcing cost

:math:`\textcolor{green}{M^{Flow}}` =                                  Big-M flow parameter

:math:`\textcolor{green}{\psi^{FracDemand}}` =                            Slack cost parameter

:math:`\textcolor{green}{\psi^{Production}}` =                            Slack cost parameter

:math:`\textcolor{green}{\psi^{Flowback}}` =                              Slack cost parameter

:math:`\textcolor{green}{\psi^{PipelineCapacity}}` =                      Slack cost parameter

:math:`\textcolor{green}{\psi^{StorageCapacity}}` =  	                   Slack cost parameter

:math:`\textcolor{green}{\psi^{DisposalCapacity}}` =                      Slack cost parameter

:math:`\textcolor{green}{\psi^{TreamentCapacity}}` =                      Slack cost parameter

:math:`\textcolor{green}{\psi^{BeneficialReuseCapacity}}` =  	           Slack cost parameter


.. _strategic_model_mathematical_program_formulation:

Strategic Model Mathematical Program Formulation
------------------------------------------------


**Objectives**

Two objective functions can be considered for the optimization of a produced water system: first, the minimization of costs, which includes operational costs associated with procurement of fresh water, the cost of disposal, trucking and piping produced water between well pads and treatment facilities, and the cost of storing, treating and reusing produced water. Capital costs are also considered due to infrastructure build out such as the installation of pipelines, treatment, and storage facilities. A credit for (re)using treated water is also considered, and additional slack variables are included to facilitate the identification of potential issues with input data. The second objective is the maximization of water reused which is defined as the ratio between the treated produced water that is used in completions operations and the total produced water coming to surface.

.. math::

    \min \ \textcolor{red}{C^{TotalSourced}}+\textcolor{red}{C^{TotalDisposal}}+\textcolor{red}{C^{TotalTreatment}}

        +\textcolor{red}{C^{TotalCompletionsReuse}}+\textcolor{red}{C^{TotalPiping}}+\textcolor{red}{C^{TotalStorage}}

        + \textcolor{red}{C^{TotalTrucking}}+\textcolor{green}{\alpha^{AnnualizationRate}} \cdot (\textcolor{red}{C^{DisposalCapEx}}

        +\textcolor{red}{C^{StorageCapEx}}+\textcolor{red}{C^{TreatmentCapEx}}+\textcolor{red}{C^{PipelineCapEx}})

        +\textcolor{red}{C^{Slack}}-\textcolor{red}{R^{TotalStorage}}


.. math::

    \max \ \textcolor{red}{F^{TotalCompletionsReuse}}/\textcolor{green}{\beta^{TotalProd}}


**Annualization Rate Calculation:**

The annualization rate is calculated using the formula described at this website: https://www.investopedia.com/terms/e/eac.asp. 
The annualization rate takes the discount rate (rate) and the number of years the CAPEX investment is expected to be used (life) as input.

.. math::
    \textcolor{green}{\alpha^{AnnualizationRate}} = \frac{\textcolor{green}{rate}}{(1-{(1+\textcolor{green}{rate})}^{-\textcolor{green}{life}})}


**Completions Pad Demand Balance:** :math:`\forall p  \in  CP, t  \in  T`

Completions pad demand can be met by trucked or piped water moved into the pad in addition to water in completions pad storage. For each completions pad and for each time period, completions demand at the given pad is equal to the sum of all piped and trucked water moved into the completions pad plus water removed from the pad storage minus water put into the pad storage plus a slack.

.. math::

    \textcolor{green}{\gamma_{p,t}^{Completions}} = \sum_{n \in N|(n,p) \in NCA}\textcolor{red}{F_{n,p,t}^{Piped}}+\sum_{\tilde{p} \in PP|(\tilde{p},p) \in PCA}\textcolor{red}{F_{\tilde{p},p,t}^{Piped}}+\sum_{s \in S|(s,p) \in SCA}\textcolor{red}{F_{s,p,t}^{Piped}}

        +\sum_{\tilde{p} \in CP|(\tilde{p},p) \in CCA}\textcolor{red}{F_{\tilde{p},p,t}^{Piped}} +\sum_{r \in R|(r,p) \in RCA}\textcolor{red}{F_{r,p,t}^{Piped}} +\sum_{f \in F|(f,p) \in FCA}\textcolor{red}{F_{f,p,t}^{Sourced}}

        +\sum_{\tilde{p} \in PP|(\tilde{p},p) \in PCT}\textcolor{red}{F_{\tilde{p},p,t}^{Trucked}} +\sum_{\tilde{p} \in CP|(\tilde{p},p) \in CCT}\textcolor{red}{F_{\tilde{p},p,t}^{Trucked}} +\sum_{s \in S|(s,p) \in SCT}\textcolor{red}{F_{s,p,t}^{Trucked}}

        +\sum_{f \in F|(f,p) \in FCT}\textcolor{red}{F_{f,p,t}^{Trucked}} +\textcolor{red}{F_{p,t}^{PadStorageOut}}-\textcolor{red}{F_{p,t}^{PadStorageIn}}+\textcolor{red}{S_{p,t}^{FracDemand}}


**Completions Pad Storage Balance:** :math:`\forall p \in CP, t \in T`

Sets the storage level at the completions pad. For each completions pad and for each time period, completions pad storage is equal to storage in last time period plus water put in minus water removed. If it is the first time period, the pad storage is the initial pad storage.

for :math:`t = 1`

.. math::

    \textcolor{red}{L_{p,t}^{PadStorage}} = \textcolor{green}{\lambda_{p,t=1}^{PadStorage}}+\textcolor{red}{F_{p,t}^{PadStorageIn}}-\textcolor{red}{F_{p,t}^{PadStorageOut}}


for :math:`t > 1`

.. math::

    \textcolor{red}{L_{p,t}^{PadStorage}} = \textcolor{red}{L_{p,t-1}^{PadStorage}}+\textcolor{red}{F_{p,t}^{PadStorageIn}}-\textcolor{red}{F_{p,t}^{PadStorageOut}}


**Completions Pad Storage Capacity:** :math:`\forall p \in CP, t \in T`

The storage at each completions pad must always be at or below its capacity in every time period.

.. math::

    \textcolor{red}{L_{p,t}^{PadStorage}} \leq \textcolor{green}{\sigma_{p}^{PadStorage}}


**Terminal Completions Pad Storage Level:** :math:`\forall p \in CP, t \in T`

The storage in the last period must be at or below its terminal storage level.

.. math::

    \textcolor{red}{L_{p,t=T}^{PadStorage}} \leq \textcolor{green}{\theta_{p}^{PadStorage}}

The storage in the last period must be at or below its terminal storage level.


**Freshwater Sourcing Capacity:** :math:`\forall f \in F, t \in T`

For each freshwater source and each time period, the outgoing water from the freshwater source is below the freshwater capacity.

.. math::

      \sum\nolimits_{(f,p) \in FCA}\textcolor{red}{F_{l,l,t}^{Sourced}} +\sum\nolimits_{(f,p) \in FCT}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{green}{\sigma_{f,t}^{Freshwater}}


**Completions Pad Truck Offloading Capacity:** :math:`\forall p \in CP, t \in T`

For each completions pad and time period, the volume of water being trucked into the completions pad must be below the trucking offloading capacity.

.. math::

    \sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(f,p) \in FCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{green}{\sigma_{p}^{Offloading,Pad}}


**Completions Pad Processing Capacity:**

For each completions pad and time period, the volume of water (excluding freshwater) coming in must be below the processing limit.

.. math::

    \sum\nolimits_{(n,p) \in NCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,p) \in PCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(s,p) \in SCA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(p,c) \in CCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(r,p) \in RCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{green}{\sigma_{p}^{Processing,Pad}}


.. note:: This constraint has not actually been implemented yet.


**Storage Site Truck Offloading Capacity:** :math:`\forall s \in S, t \in T`

For each storage site and each time period, the volume of water being trucked into the storage site must be below the trucking offloading capacity for that storage site.

.. math::

    \sum\nolimits_{(p,s) \in PST}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,s) \in CST}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{green}{\sigma_{s}^{Offloading,Storage}}


**Storage Site Processing Capacity:** :math:`\forall s \in S, t \in T`

For each storage site and each time period, the volume of water being trucked into the storage site must be less than the processing capacity for that storage site.

.. math::

    \sum\nolimits_{(n,s) \in NSA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(r,s) \in RSA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,s) \in PST}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,s) \in CST}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{green}{\sigma_{s}^{Processing,Storage}}


**Production Pad Supply Balance:** :math:`\forall p \in PP, t \in T`

All produced water must be accounted for. For each production pad and for each time period, the volume of outgoing water must be equal to the forecasted produced water for the production pad.

.. math::

    \textcolor{green}{\beta_{p,t}^{Production}} = \sum\nolimits_{(p,n) \in PNA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,p) \in PCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in PPA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(p,k) \in PKT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(p,s) \in PST}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,r) \in PRT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,o) \in POT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\textcolor{red}{S_{p,t}^{Production}}



**Completions Pad Supply Balance (i.e. Flowback Balance):** :math:`\forall p \in CP, t \in T`

All flowback water must be accounted for.  For each completions pad and for each time period, the volume of outgoing water must be equal to the forecasted flowback produced water for the completions pad.

.. math::

    \textcolor{green}{\beta_{p,t}^{Flowback}} = \sum\nolimits_{(p,n) \in CNA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,c) \in CCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

    +\sum\nolimits_{(p,k) \in CKT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(p,s) \in CST}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(p,r) \in CRT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\textcolor{red}{S_{p,t}^{Flowback}}



**Network Node Balance:** :math:`\forall n \in N, t \in T`

Flow balance constraint (i.e., inputs are equal to outputs). For each pipeline node and for each time period, the volume water into the node is equal to the volume of water out of the node.

.. math::

    \sum\nolimits_{(p,n) \in PNA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,n) \in CNA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(\tilde{n},n) \in NNA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,n) \in SNA}\textcolor{red}{F_{l,l,t}^{Piped}}

        = \sum\nolimits_{(n,\tilde{n}) \in NNA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,p) \in NCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(n,k) \in NKA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(n,r) \in NRA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,s) \in NSA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,o) \in NOA}\textcolor{red}{F_{l,l,t}^{Piped}}



**Bi-Directional Flow:** :math:`\forall (l,l) \in {PCA,PNA,PPA,CNA,NNA,NCA,NKA,NSA,NRA, \ldots ,SOA}, t \in T`

There can only be flow in one direction for a given pipeline arc in a given time period. Flow is only allowed in a given direction if the binary indicator for that direction is "on".


.. math::

    \textcolor{red}{y_{l,\tilde{l},t}^{Flow}}+\textcolor{red}{y_{\tilde{l},l,t}^{Flow}} = 1

.. note:: Technically this constraint should only be enforced for truly reversible arcs (e.g. NCA and CNA); and even then it only needs to be defined per one reversible arc (e.g. NCA only and not NCA and CNA).

.. math::

    \textcolor{red}{F_{l,l,t}^{Piped}} \leq \textcolor{red}{y_{l,l,t}^{Flow}} \cdot \textcolor{green}{M^{Flow}}



**Storage Site Balance:** :math:`\forall s \in S, t \in T`

For each storage site and for each time period, if it is the first time period, the storage level is the initial storage. Otherwise, the storage level is equal to the storage level in the previous time period plus water inputs minus water outputs.

.. math::

    \textcolor{red}{L_{s,t}^{Storage}} = \textcolor{green}{\lambda_{s,t=1}^{Storage}}+\textcolor{red}{L_{s,t-1}^{Storage}}+\sum\nolimits_{(n,s) \in NSA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(r,s) \in RSA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,s) \in PST}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,s) \in CST}\textcolor{red}{F_{l,l,t}^{Trucked}}-\sum\nolimits_{(s,n) \in SNA}\textcolor{red}{F_{l,l,t}^{Piped}}-\sum\nolimits_{(s,p) \in SCA}\textcolor{red}{F_{l,l,t}^{Piped}}-\sum\nolimits_{(s,k) \in SKA}\textcolor{red}{F_{l,l,t}^{Piped}}

        -\sum\nolimits_{(s,r) \in SRA}\textcolor{red}{F_{l,l,t}^{Piped}}-\sum\nolimits_{(s,o) \in SOA}\textcolor{red}{F_{l,l,t}^{Piped}}-\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}}-\sum\nolimits_{(s,k) \in SKT}\textcolor{red}{F_{l,l,t}^{Trucked}}



**Terminal Storage Level:** :math:`\forall s \in S, t \in T`

For each storage site, the storage in the last time period must be less than or equal to the predicted/set terminal storage level.

.. math::

    \textcolor{red}{L_{s,t=T}^{Storage}} \leq \textcolor{green}{\theta_{s}^{Storage}}



**Network Node Capacity:** :math:`\forall n \in N, t \in T`

Flow capacity constraint. For each pipeline node and for each time period, the volume should not exceed the node capacity.

.. math::

    \sum\nolimits_{(p,n) \in PNA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,n) \in CNA}\textcolor{red}{F_{l,l,t}^{Piped}} 
    
    +\sum\nolimits_{(\tilde{n},n) \in NNA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,n) \in SNA}\textcolor{red}{F_{l,l,t}^{Piped}}

        \leq \textcolor{green}{\sigma_{n}^{Node}}



**Pipeline Capacity Construction Expansion:** :math:`\forall {l,l} \in {PCA,PNA,PPA,NKA,CNA,NCA,NSA,NOA,FCA,RCA,SKA,SOA,RSA,SRA}, [t \in T]`

Sets the flow capacity in a given pipeline during a given time period. Different constraints apply depending on if the pipeline is realistically reversible or not.

.. math::

    \textcolor{red}{F_{l,\tilde{l},[t]}^{Capacity}} = \textcolor{green}{\sigma_{l,\tilde{l}}^{Pipeline}}+\sum\nolimits_{d \in D}\textcolor{green}{\delta_{d}^{Pipeline}} \cdot \textcolor{red}{y_{l,\tilde{l},d}^{Pipeline}}+\textcolor{red}{S_{l,\tilde{l}}^{PipelineCapacity}}

:math:`\forall (l,l) \in {PPA,CNA,NNA,NCA,NSA,NRA,RNA,RKA,SNA,SCA},[t \in T]`

.. math::

    \textcolor{red}{F_{l,\tilde{l},[t]}^{Capacity}} = \textcolor{green}{\sigma_{l,\tilde{l}}^{Pipeline}}+\sum\nolimits_{d \in D}\textcolor{green}{\delta_{d}^{Pipeline}} \cdot (\textcolor{red}{y_{l,\tilde{l},d}^{Pipeline}}+\textcolor{red}{y_{\tilde{l},l,d}^{Pipeline}} )+\textcolor{red}{S_{l,\tilde{l}}^{PipelineCapacity}}

.. note::

    :math:`\delta` can be input by user or calculated. If the user chooses to calculate pipeline capacity, the parameter will be calculated by the equation below where :math:`{\kappa_{l,l}}` is Hazen-Williams constant and :math:`\omega` is Hazen-Williams exponent as per Cafaro & Grossmann (2021) and d represents the pipeline diameter as per the set :math:`d \in D`.

    See equation:

.. math::

    \textcolor{green}{\delta_{d}^{Pipeline}} = {\kappa_{l,l}} \cdot \textcolor{blue}{d}^{\omega}


:math:`\forall {l,l} \in {PCA,PNA,PPA,CNA,RCA NNA,NCA,NKA,NSA,NRA, \ldots ,SOA}, t \in T`

.. math::

    \textcolor{red}{F_{l,l,t}^{Piped}} \leq \textcolor{red}{F_{l,l,[t]}^{Capacity}}


**Storage Capacity Construction/Expansion:** :math:`\forall s \in S, [t \in T]`

This constraint accounts for the expansion of available storage capacity or installation of storage facilities. If expansion/construction is selected, expand the capacity by the set expansion amount. The water level at the storage site must be less than this capacity. As of now, the model considers that a storage facility is expanded or built at the beginning of the planning horizon. The C0 notation indicates that we also include the 0th case, meaning that there is no selection in the set C where no capacity is added.

.. math::

    \textcolor{red}{X_{s,[t]}^{Capacity}} = \textcolor{green}{\sigma_{s}^{Storage}}+\sum\nolimits_{c \in C_0}\textcolor{green}{\delta_{c}^{Storage}} \cdot \textcolor{red}{y_{s,c}^{Storage}}+\textcolor{red}{S_{s}^{StorageCapacity}}

:math:`\forall s \in S, t \in T`

.. math::

    \textcolor{red}{L_{s,t}^{Storage}} \leq \textcolor{red}{X_{s,[t]}^{Capacity}}



**Disposal Capacity Construction/Expansion:** :math:`\forall k \in K, [t \in T]`

This constraint accounts for the expansion of available disposal sites or installation of new disposal sites. If expansion/construction is selected, expand the capacity by the set expansion amount. The total disposed water in a given time period must be less than this new capacity.

.. math::

    \textcolor{red}{D_{k,[t]}^{Capacity}} = \textcolor{green}{\sigma_{k}^{Disposal}}+\sum\nolimits_{i \in I_0}\textcolor{green}{\delta_{i}^{Disposal}} \cdot \textcolor{red}{y_{k,i}^{Disposal}}+\textcolor{red}{S_{k}^{DisposalCapacity}}

:math:`\forall k \in K, t \in T`

.. math::

    \sum\nolimits_{(n,k) \in NKA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(s,k) \in SKA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(s,k) \in SKT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,k) \in PKT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,k) \in CKT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(r,k) \in RKT}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{red}{D_{k,[t]}^{Capacity}}



**Treatment Capacity Construction/Expansion:** :math:`\forall r \in R, [t \in T]`

Similarly to Disposal and Storage Capacity Construction/Expansion constraints, the current treatment capacity can be expanded as required or new facilities may be installed.

.. math::

    \textcolor{red}{T_{r,[t]}^{Capacity}} = \textcolor{green}{\sigma_{r}^{Treatment}}+\sum\nolimits_{j \in J_0}\textcolor{green}{\delta_{j}^{Treatment}} \cdot \textcolor{red}{y_{r,j}^{Treatment}}+\textcolor{red}{S_{r}^{TreatmentCapacity}}

:math:`\forall r \in R, t \in T`

.. math::

    \sum\nolimits_{(n,r) \in NRA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(s,r) \in SRA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,r) \in PRT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,r) \in CRT}\textcolor{red}{F_{l,l,t}^{Trucked}} \leq \textcolor{red}{T_{r,[t]}^{Capacity}}


**Treatment Balance:** :math:`\forall r \in R, t \in T`

Water input into treatment facility is treated with a level of efficiency, meaning only a given percentage of the water input is outputted to be reused at the completions pads.

.. math::

    \textcolor{green}{\epsilon_{r, \textcolor{green}{W_{r}^{TreatmentComponent}}}^{Treatment}} \cdot (\sum\nolimits_{(n,r) \in NRA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,r) \in SRA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,r) \in PRT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,r) \in CRT}\textcolor{red}{F_{l,l,t}^{Trucked}} )=\sum\nolimits_{(r,p) \in RCA}\textcolor{red}{F_{l,l,t}^{Piped}} + \textcolor{red}{F_{r,t}^{UnusedTreatedWater}}

where :math:`\textcolor{green}{\epsilon_{r, w}^{Treatment}}` < 1



**Beneficial Reuse Capacity:** :math:`\forall o \in O, t \in T`

For each beneficial reuse site and for each time period, water sent to a site must be less than or equal to the capacity.

.. math::

    \sum\nolimits_{(n,o) \in NOA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(s,o) \in SOA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,o) \in POT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        \leq \textcolor{green}{\sigma_{o}^{BeneficialReuse}}+\textcolor{red}{S_{o}^{BeneficialReuseCapacity}}



**Fresh Sourcing Cost:** :math:`\forall f \in F, p \in CP, t \in T`

For each freshwater source, for each completions pad, and for each time period, the freshwater sourcing cost is equal to all output from the freshwater source times the freshwater sourcing cost.

.. math::

    \textcolor{red}{C_{f,p,t}^{Sourced}} =(\textcolor{red}{F_{f,p,t}^{Sourced}}+\textcolor{red}{F_{f,p,t}^{Trucked}})\cdot \textcolor{green}{\pi_{f}^{Sourcing}}

    \textcolor{red}{C^{TotalSourced}} = \sum\nolimits_{t \in T}\sum\nolimits_{(f,p) \in FCA}\textcolor{red}{C_{f,p,t}^{Sourced}}



**Total Fresh Sourced Volume:**

The total fresh sourced volume is the sum of freshwater movements by truck and pipeline over all time periods, completions pads, and freshwater sources.

.. math::

    \textcolor{red}{F^{TotalSourced}} = \sum\nolimits_{t \in T}\sum\nolimits_{f \in F}\sum\nolimits_{p \in CP}(\textcolor{red}{F_{f,p,t}^{Sourced}}+\textcolor{red}{F_{f,p,t}^{Trucked}})



**Disposal Cost:** :math:`\forall k \in K, t \in T`

For each disposal site, for each time period, the disposal cost is equal to all water moved into the disposal site multiplied by the operational disposal cost. Total disposal cost is the sum of disposal costs over all time periods and all disposal sites.

.. math::

       \textcolor{red}{C_{k,t}^{Disposal}} = (\sum\nolimits_{(l,k) \in {NKA,RKA,SKA}}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(l,k) \in {PKT,CKT,SKT,RKT}}\textcolor{red}{F_{l,l,t}^{Trucked}}) \cdot \textcolor{green}{\pi_{k}^{Disposal}}

       \textcolor{red}{C^{TotalDisposal}} = \sum\nolimits_{t \in T}\sum\nolimits_{k \in K}\textcolor{red}{C_{k,t}^{Disposal}}



**Total Disposed Volume:**

Total disposed volume over all time is the sum of all piped and trucked water to disposal summed over all time periods.

.. math::

    \textcolor{red}{F^{TotalDisposed}} = \sum\nolimits_{t \in T}(\sum\nolimits_{(l,l) \in {NKA,RKA,SKA}}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(l,l) \in {PKT,CKT,SKT,RKT}}\textcolor{red}{F_{l,l,t}^{Trucked}})



**Treatment Cost:** :math:`\forall r \in R, t \in T`

For each treatment site, for each time period, the treatment cost is equal to all water moved to the treatment site multiplied by the operational treatment cost. The total treatments cost is the sum of treatment costs over all time periods and all treatment sites.

.. math::

    \textcolor{red}{C_{r,t}^{Treatment}} = (\sum\nolimits_{(l,l) \in {NRA,SRA}}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(l,l) \in {PRT,CRT}}\textcolor{red}{F_{l,l,t}^{Trucked}}) \cdot \textcolor{green}{\pi_{r}^{Treatment}}

    \textcolor{red}{C^{TotalTreatment}} = \sum\nolimits_{t \in T}\sum\nolimits_{r \in R}\textcolor{red}{C_{r,t}^{Treatment}}



**Completions Reuse Cost:** :math:`\forall p \in P, t \in T`

Completions reuse water is all water that meets completions pad demand, excluding freshwater. Completions reuse cost is the volume of completions reused water multiplied by the cost for reuse.

.. math::

    \textcolor{red}{C_{p,t}^{CompletionsReuse}} = (\sum\nolimits_{(n,p) \in NCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in PCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(r,p) \in RCA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(s,p) \in SCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,c) \in CCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}}) \cdot \textcolor{green}{\pi_{p}^{CompletionsReuse}}


.. note:: Freshwater sourcing is excluded from completions reuse costs.

.. math::

    \textcolor{red}{C^{TotalReuse}} = \sum\nolimits_{t \in T}\sum\nolimits_{p \in CP}\textcolor{red}{C_{p,t}^{Reuse}}



**Total Completions Reuse Volume:**

The total reuse volume is the total volume of produced water reused, or the total water meeting completions pad demand over all time periods, excluding freshwater.

.. math::

    \textcolor{red}{F^{TotalCompletionsReused}} = \sum\nolimits_{t \in T}(\sum\nolimits_{(n,p) \in NCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,p) \in PCA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(s,p) \in SCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(r,p) \in RCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(p,p) \in CCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}})



**Piping Cost:** :math:`\forall (l,l) \in {PPA, \ldots ,CCA}, t \in T`

Piping cost is the total volume of piped water multiplied by the cost for piping.

.. math::

    \textcolor{red}{C_{l,l,t}^{Piped}} = (\textcolor{red}{F_{l,l,t}^{Piped}}+\textcolor{red}{F_{l,l,t}^{Sourced})} \cdot \textcolor{green}{\pi_{l,l}^{Pipeline}}

    \textcolor{red}{C^{TotalPiping}} = \sum\nolimits_{t \in T}\sum\nolimits_{(l,l) \in {PPA, \ldots}}\textcolor{red}{C_{l,l,t}^{Piped}}


.. note:: The constraints above explicitly consider freshwater piping via FCA arcs.



**Storage Deposit Cost:** :math:`\forall s \in S, t \in T`

Cost of depositing into storage is equal to the total volume of water moved into storage multiplied by the storage operation cost rate.

.. math::

    \textcolor{red}{C_{s,t}^{Storage}} = (\sum\nolimits_{(l,s) \in {NSA}}\textcolor{red}{F_{l,s,t}^{Piped}} +\sum\nolimits_{(l,s) \in {RSA}}\textcolor{red}{F_{l,s,t}^{Piped}}

        +\sum\nolimits_{(l,s) \in {CST}}\textcolor{red}{F_{l,s,t}^{Trucked}}+\sum\nolimits_{(l,s) \in {PST}}\textcolor{red}{F_{l,s,t}^{Trucked}}) \cdot \textcolor{green}{\pi_{s}^{Storage}}

    \textcolor{red}{C^{TotalStorage}} = \sum\nolimits_{t \in T}\sum\nolimits_{s \in S}\textcolor{red}{C_{s,t}^{Storage}}



**Storage Withdrawal Credit:** :math:`\forall s \in S, t \in T`

Credits from withdrawing from storage is equal to the total volume of water moved out from storage multiplied by the storage operation credit rate.

.. math::

    \textcolor{red}{R_{s,t}^{Storage}} = (\sum\nolimits_{(s,l) \in {SNA,SCA,SKA,SRA,SOA}}\textcolor{red}{F_{s,l,t}^{Piped}}+\sum\nolimits_{(s,l) \in {SCT,SKT}}\textcolor{red}{F_{s,l,t}^{Trucked}}) \cdot \textcolor{green}{\rho_{s}^{Storage}}

    \textcolor{red}{R^{TotalStorage}} = \sum\nolimits_{t \in T}\sum\nolimits_{s \in S}\textcolor{red}{R_{s,t}^{Storage}}



**Pad Storage Cost:** :math:`\forall l \in L, \tilde{l} \in L, t \in T`

**Trucking Cost (Simplified)**

Trucking cost between two locations for time period is equal to the trucking volume between locations in time t divided by the truck capacity [this gets # of truckloads] multiplied by the lead time between two locations and hourly trucking cost.

.. math::

    \textcolor{red}{C_{l,\tilde{l},t}^{Trucked}} = \textcolor{red}{F_{l,\tilde{l},t}^{Trucked}} \cdot \textcolor{green}{1 / \delta^{Truck}}  \cdot\textcolor{green}{\tau_{l,\tilde{l}}^{Trucking}} \cdot \textcolor{green}{\pi_{l}^{Trucking}}

    \textcolor{red}{C^{TotalTrucking}} = \sum\nolimits_{t \in T}\sum\nolimits_{(l,l) \in {PPA, \ldots ,CCT}}\textcolor{red}{C_{l,\tilde{l},t}^{Trucked}}


.. note:: The constraints above explicitly consider freshwater trucking via FCT arcs.




**Total Trucking Volume:** :math:`\forall t \in T`

The total trucking volume is estimated as the summation of trucking movements over all time periods and locations.

.. math::

    \textcolor{red}{F^{TotalTrucking}} = \sum\nolimits_{t \in T}\sum\nolimits_{(l,\tilde{l}) \in {PPA, \ldots ,CCT}}\textcolor{red}{F_{l,\tilde{l},t}^{Trucked}}



**Disposal Construction or Capacity Expansion Cost:** :math:`\forall t \in T`

Cost related to expanding or constructing new disposal capacity. Takes into consideration capacity increment, cost for selected capacity increment, and if the construction/expansion is selected to occur.

.. math::

    \textcolor{red}{C_{[t]}^{DisposalCapEx}} = \sum\nolimits_{i \in I_0} \sum\nolimits_{k \in K}\textcolor{green}{\kappa_{k,i}^{Disposal}} \cdot\textcolor{green}{\delta_{i}^{Disposal}} \cdot \textcolor{red}{y_{k,i}^{Disposal}}



**Storage Construction or Capacity Expansion Cost:** :math:`\forall t \in T`

Cost related to expanding or constructing new storage capacity. Takes into consideration capacity increment, cost for selected capacity increment, and if the construction/expansion is selected to occur.

.. math::

    \textcolor{red}{C_{[t]}^{StorageCapEx}} = \sum\nolimits_{s \in S} \sum\nolimits_{c \in C_0}\textcolor{green}{\kappa_{s,c}^{Storage}} \cdot \textcolor{green}{\delta_{c}^{Storage}} \cdot \textcolor{red}{y_{s,c}^{Storage}}



**Treatment Construction or Capacity Expansion Cost:** :math:`\forall t \in T`

Cost related to expanding or constructing new treatment capacity. Takes into consideration capacity increment, cost for selected capacity increment, and if the construction/expansion is selected to occur.

.. math::

    \textcolor{red}{C_{[t]}^{TreatmentCapEx}} = \sum\nolimits_{r \in R}\sum\nolimits_{j \in J_0}\textcolor{green}{\kappa_{r,j}^{Treatment}} \cdot \textcolor{green}{\delta_{j}^{Treatment}} \cdot \textcolor{red}{y_{r,j}^{Treatment}}



**Pipeline Construction or Capacity Expansion Cost:** :math:`\forall t \in T`

Cost related to expanding or constructing new pipeline capacity is calculated differently depending on model configuration settings.


If the pipeline cost configuration is **capacity based**, pipeline expansion cost is calculated using capacity increments, cost for selected capacity increment, and if the construction/expansion is selected to occur.

.. math::

    \textcolor{red}{C_{[t]}^{PipelineCapEx}} = \sum\nolimits_{l \in L}\sum\nolimits_{l \in L}\sum\nolimits_{d \in D_0}\textcolor{green}{\kappa_{l,l,d}^{Pipeline}} \cdot \textcolor{green}{\delta_{d}^{Pipeline}} \cdot \textcolor{red}{y_{l,l,d}^{Pipeline}}

If the pipeline cost configuration is **distance based**, pipeline expansion cost is calculated using pipeline distances, pipeline diameters, cost per inch mile, and if the construction/expansion is selected to occur.

.. math::

    \textcolor{red}{C_{[t]}^{PipelineCapEx}} = \sum\nolimits_{l \in L}\sum\nolimits_{l \in L}\sum\nolimits_{d \in D_0}\textcolor{green}{\kappa^{Pipeline} \cdot }\textcolor{green}{\mu_{d}^{Pipeline}} \cdot \textcolor{green}{\lambda_{l,l}^{Pipeline}} \cdot \textcolor{red}{y_{l,l,d}^{Pipeline}}



**Slack Costs:**

Weighted sum of the slack variables. In the case that the model is infeasible, these slack variables are used to determine where the infeasibility occurs (e.g. pipeline capacity is not sufficient).

.. math::

    \textcolor{red}{C^{Slack}} = \sum\nolimits_{p \in CP}\sum\nolimits_{t \in T}\textcolor{red}{S_{p,t}^{FracDemand}} \cdot \textcolor{green}{\psi^{FracDemand}}+\sum\nolimits_{p \in PP}\sum\nolimits_{t \in T}\textcolor{red}{S_{p,t}^{Production}}  \cdot \textcolor{green}{\psi^{Production}}

        +\sum\nolimits_{p \in CP}\sum\nolimits_{t \in T}\textcolor{red}{S_{p,t}^{Flowback}} \cdot \textcolor{green}{\psi^{Flowback}}+\sum\nolimits_{(l,l) \in { \ldots }}\textcolor{red}{S_{l,l}^{PipelineCapacity}}  \cdot \textcolor{green}{\psi^{PipeCapacity}}

         +\sum\nolimits_{s \in S}\textcolor{red}{S_{s}^{StorageCapacity}}  \cdot \textcolor{green}{\psi^{StorageCapacity}}+\sum\nolimits_{k \in K}\textcolor{red}{S_{k}^{DisposalCapacity}} \cdot \textcolor{green}{\psi^{DisposalCapacity}}

         +\sum\nolimits_{r \in R}\textcolor{red}{S_{r}^{TreatmentCapacity}} \cdot \textcolor{green}{\psi^{TreatmentCapacity}}+\sum\nolimits_{o \in O}\textcolor{red}{S_{o}^{BeneficialReuseCapacity}}  \cdot \textcolor{green}{\psi^{BeneficialReuseCapacity}}



**Logic Constraints:** :math:`\forall k \in K`

New pipeline or facility capacity constraints: e.g., only one injection capacity can be used for a given site

.. math::

    \sum\nolimits_{i \in I_0}\textcolor{red}{y_{k,i,[t]}^{Disposal}} = 1

:math:`\forall s \in S`

.. math::

    \sum\nolimits_{c \in C_0}\textcolor{red}{y_{s,c,[t]}^{Storage}} = 1

:math:`\forall r \in R`

.. math::

    \sum\nolimits_{j \in J_0}\textcolor{red}{y_{r,j,[t]}^{Treatment}} = 1

:math:`\forall l \in L, l \in L`

.. math::

    \sum\nolimits_{d \in D_0}\textcolor{red}{y_{l,l,d,[t]}^{Pipeline}} = 1


**Deliveries Destination Constraints:**

Completions reuse deliveries at a completions pad in time period t is equal to all piped and trucked water moved into the completions pad, excluding freshwater.
:math:`\forall p \in CP, t \in T`

.. math::

    \textcolor{red}{F_{p,t}^{CompletionsReuseDestination}} = \sum\nolimits_{l \in {P,N,R,S}}\textcolor{red}{F_{l,p,t}^{Piped}}+\textcolor{red}{F_{l,p,t}^{Trucked}}

Disposal deliveries for disposal site k at time t is equal to all piped and trucked water moved to the disposal site k.
:math:`\forall k \in K, t \in T`

.. math::

    \textcolor{red}{F_{k,t}^{DisposalDestination}} = \sum\nolimits_{l \in L}\textcolor{red}{F_{l,k,t}^{Piped}}+\textcolor{red}{F_{l,k,t}^{Trucked}}

Completions deliveries destination for completions pad p at time t is equal to all piped and trucked water moved to the completions pad.
:math:`\forall p \in CP, t \in T`

.. math::

    \textcolor{red}{F_{p,t}^{CompletionsDestination}}  = \sum\nolimits_{(n,p) \in NCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in PCA}\textcolor{red}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,p) \in SCA}\textcolor{red}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(p,c) \in CCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(r,p) \in RCA}\textcolor{red}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(f,p) \in FCA}\textcolor{red}{F_{l,l,t}^{Sourced}}

        +\sum\nolimits_{(p,p) \in PCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(s,p) \in SCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,p) \in CCT}\textcolor{red}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(f,p) \in FCT}\textcolor{red}{F_{l,l,t}^{Trucked}} +\textcolor{red}{F_{p,t}^{PadStorageOut}}-\textcolor{red}{F_{p,t}^{PadStorageIn}}

.. _strategic_model_water_quality_extension:

Strategic Model Water Quality Extension
---------------------------------------------------
An extension to this strategic optimization model measures the water quality across all locations over time. As of now, water quality is not a decision variable. It is calculated after optimization of the strategic model.
The process for calculating water quality is as follows: the strategic model is first solved to optimality, water quality variables and constraints are added, flow rates and storage levels are fixed to the solved values at optimality, and the water quality is calculated.

.. note:: Fixed variables are denoted in purple in the documentation.

Assumptions:

* Water quality of produced water from production pads and completions pads remains the same across all time periods
* When blending flows of different water quality, they blend linearly
* Treatment does not affect water quality

**Water Quality Sets**

:math:`\textcolor{blue}{w \in W}`			                     Water Quality Components (e.g., TDS)

:math:`\textcolor{blue}{p^{IntermediateNode} \in CP}`			 Intermediate Completions Pad Nodes

:math:`\textcolor{blue}{p^{PadStorage} \in CP}`			     Pad Storage


**Water Quality Parameters**

:math:`\textcolor{green}{v_{l,w,[t]}}` = 	                Water quality at well pad

:math:`\textcolor{green}{\xi_{l,w}^{StorageSite}}` = 	        Initial water quality at storage

:math:`\textcolor{green}{\xi_{l,w}^{PadStorage}}` = 	        Initial water quality at pad storage


**Water Quality Variables**

:math:`\textcolor{red}{Q_{l,w,t}}` =           Water quality at location


**Disposal Site Water Quality** :math:`\forall k \in K, w \in W, t \in T`

The water quality of disposed water is dependent on the flow rates into the disposal site and the quality of each of these flows.

.. math::

    \sum\nolimits_{(n,k) \in NKA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{n,w,t}} +\sum\nolimits_{(s,k) \in SKA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{s,w,t}}+\sum\nolimits_{(r,k) \in RKA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{r,w,t}}

    +\sum\nolimits_{(s,k) \in SKT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{red}{Q_{s,w,t}}+\sum\nolimits_{(p,k) \in PKT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}}

    +\sum\nolimits_{(p,k) \in CKT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}}+\sum\nolimits_{(r,k) \in RKT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{red}{Q_{r,w,t}}

    =\textcolor{purple}{F_{k,t}^{DisposalDestination}} \cdot \textcolor{red}{Q_{k,w,t}}

**Storage Site Water Quality** :math:`\forall s \in S, w \in W, t \in T`

The water quality at storage sites is dependent on the flow rates into the storage site, the volume of water in storage in the previous time period, and the quality of each of these flows. Even mixing is assumed, so all outgoing flows have the same water quality. If it is the first time period, the initial storage level and initial water quality replaces the water stored and water quality in the previous time period respectively.

.. math::

    \textcolor{green}{\lambda_{s,t=1}^{Storage}} \cdot \textcolor{green}{\xi_{l,w}^{StorageSite}} +\textcolor{purple}{L_{s,t-1}^{Storage}} \cdot \textcolor{red}{Q_{s,w,t-1}} +\sum\nolimits_{(n,s) \in NSA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{n,w,t}}

    +\sum\nolimits_{(p,s) \in PST}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}} +\sum\nolimits_{(p,s) \in CST}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}}

    = \textcolor{red}{Q_{s,w,t}} \cdot (\textcolor{purple}{L_{s,t}^{Storage}} +\sum\nolimits_{(s,n) \in SNA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,p) \in SCA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,k) \in SKA}\textcolor{purple}{F_{l,l,t}^{Piped}}

    +\sum\nolimits_{(s,r) \in SRA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,o) \in SOA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,p) \in SCT}\textcolor{purple}{F_{l,l,t}^{Trucked}}+\sum\nolimits_{(s,k) \in SKT}\textcolor{purple}{F_{l,l,t}^{Trucked}})

**Treatment Site Water Quality** :math:`\forall r \in R, w \in W, t \in T`

The water quality at treatment sites is dependent on the flow rates into the treatment site, the efficiency of treatment, and the water quality of the flows. Even mixing is assumed, so all outgoing flows have the same water quality. The treatment process does not affect water quality

.. math::

    \textcolor{green}{\epsilon_{r,\textcolor{green}{W_{r}^{TreatmentComponent}}}^{Treatment}} \cdot (\sum\nolimits_{(n,r) \in NRA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{n,w,t}} +\sum\nolimits_{(s,r) \in SRA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{s,w,t}}

    +\sum\nolimits_{(p,r) \in PRT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}} +\sum\nolimits_{(p,r) \in CRT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}} )

    = \textcolor{red}{Q_{r,w,t}} \cdot (\sum\nolimits_{(r,p) \in RCA}\textcolor{purple}{F_{l,l,t}^{Piped}} + \textcolor{purple}{F_{r,t}^{UnusedTreatedWater}})

where :math:`\textcolor{green}{\epsilon_{r,w}^{Treatment}}` <1

**Network Node Water Quality** :math:`\forall n \in N, w \in W, t \in T`

The water quality at nodes is dependent on the flow rates into the node and the water quality of the flows. Even mixing is assumed, so all outgoing flows have the same water quality.

.. math::

    \sum\nolimits_{(p,n) \in PNA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{green}{v_{p,w,[t]}} +\sum\nolimits_{(p,n) \in CNA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{green}{v_{p,w,[t]}}

    +\sum\nolimits_{(\tilde{n},n) \in NNA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{n,w,t}}+\sum\nolimits_{(s,n) \in SNA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{s,w,t}}

    = \textcolor{red}{Q_{n,w,t}} \cdot (\sum\nolimits_{(n,\tilde{n}) \in NNA}\textcolor{purple}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,p) \in NCA}\textcolor{purple}{F_{l,l,t}^{Piped}}

    +\sum\nolimits_{(n,k) \in NKA}\textcolor{purple}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,r) \in NRA}\textcolor{purple}{F_{l,l,t}^{Piped}}

    +\sum\nolimits_{(n,s) \in NSA}\textcolor{purple}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(n,o) \in NOA}\textcolor{purple}{F_{l,l,t}^{Piped}})

.. admonition:: Water Quality at Completions Pads

    Water that is Piped and Trucked to a completions pad is mixed and split into two output streams: Stream (1) goes to the completions pad and stream (2) is input to the completions storage.
    This mixing happens at an intermediate node. Finally, water that meets completions demand comes from two inputs: The first input is output stream (1) from the intermediate step. The second is outgoing flow from the storage tank.

**Completions Pad Intermediate Node Water Quality** :math:`\forall p \in P, w \in W, t \in T`

The water quality at the completions pad intermediate node is dependent on the flow rates of water from outside of the pad to the pad. Even mixing is assumed, so the water to storage and water to completions input have the same water quality.

.. math::

    \sum\nolimits_{(n,p) \in NCA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(p,p) \in PCA}\textcolor{purple}{F_{l,l,t}^{Piped}}+\sum\nolimits_{(s,p) \in SCA}\textcolor{purple}{F_{l,l,t}^{Piped}}

        +\sum\nolimits_{(p,c) \in CCA}\textcolor{purple}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(r,p) \in RCA}\textcolor{purple}{F_{l,l,t}^{Piped}} +\sum\nolimits_{(f,p) \in FCA}\textcolor{purple}{F_{l,l,t}^{Sourced}}

        +\sum\nolimits_{(p,p) \in PCT}\textcolor{purple}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(s,p) \in SCT}\textcolor{purple}{F_{l,l,t}^{Trucked}} +\sum\nolimits_{(p,p) \in CCT}\textcolor{purple}{F_{l,l,t}^{Trucked}}

        +\sum\nolimits_{(f,p) \in FCT}\textcolor{purple}{F_{l,l,t}^{Trucked}} = \textcolor{red}{Q_{p^{IntermediateNode},w,t}} \cdot  ( \textcolor{purple}{F_{p,t}^{PadStorageIn}} + \textcolor{purple}{F_{p,t}^{CompletionsDestination}})



**Completions Pad Input Node Water Quality** :math:`\forall p \in P, w \in W, t \in T`

The water quality at the completions pad input is dependent on the flow rates of water from pad storage and water from the intermediate node. Even mixing is assumed, so all water into the pad is of the same water quality.

.. math::

    \textcolor{purple}{F_{p,t}^{PadStorageOut}} \cdot \textcolor{red}{Q_{p^{PadStorage},w,t}}+\textcolor{purple}{F_{p,t}^{CompletionsDestination}} \cdot \textcolor{red}{Q_{p^{IntermediateNode},w,t}}

    = \textcolor{red}{Q_{p,w,t}} \cdot \textcolor{green}{\gamma_{p,t}^{Completions}}


**Completions Pad Storage Node Water Quality** :math:`\forall p \in P, w \in W, t \in T`

The water quality at pad storage sites is dependent on the flow rates into the pad storage site, the volume of water in pad storage in the previous time period, and the quality of each of these flows. Even mixing is assumed, so the outgoing flow to completions pad and water in storage at the end of the period have the same water quality. If it is the first time period, the initial storage level and initial water quality replaces the water stored and water quality in the previous time period, respectively.


.. math::

    \textcolor{green}{\lambda_{s,t=1}^{PadStorage}} \cdot \textcolor{green}{\xi_{l,w}^{PadStorage}} +\textcolor{purple}{L_{s,t-1}^{PadStorage}} \cdot \textcolor{red}{Q_{p^{PadStorage},w,t-1}}

    + \textcolor{purple}{F_{p,t}^{PadStorageIn}}  \cdot \textcolor{red}{Q_{p^{IntermediateNode},w}}

    = \textcolor{red}{Q_{p^{PadStorage},w,t}} \cdot (\textcolor{purple}{L_{s,t}^{PadStorage}} + \textcolor{purple}{F_{p,t}^{PadStorageOut}} )


**Beneficial Reuse Water Quality** :math:`\forall o \in O, w \in W, t \in T`

The water quality at beneficial reuse sites is dependent on the flow rates into the site and the water quality of the flows.

.. math::

    \sum\nolimits_{(n,o) \in NOA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{n,w,t}} +\sum\nolimits_{(s,o) \in SOA}\textcolor{purple}{F_{l,l,t}^{Piped}} \cdot \textcolor{red}{Q_{s,w,t}} +\sum\nolimits_{(p,o) \in POT}\textcolor{purple}{F_{l,l,t}^{Trucked}} \cdot \textcolor{green}{v_{p,w,[t]}}

    = \textcolor{red}{Q_{o,w,t}} \cdot \textcolor{purple}{F_{o,t}^{BeneficialReuseDestination}}


.. _strategic_model_references:

References
----------

Cafaro, D. C., & Grossmann, I. (2021). Optimal design of water pipeline networks for the development of shale gas resources. AIChE Journal, 67(1), e17058.