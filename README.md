# CTI in a Box

This project is intended to provide a set of guides, tools and resources to establish a Cyber Threat Intelligence Program from scratch when your starting budget is $0.

This project includes resources for you to:
- Pitching a cyber threat intelligence program at your company to establish a CTI function
- Design your cyber threat intelligence program including developing Intelligence Requirements (IRs) and Priority Intelligence Requirements (PIRs)
- Assess the maturity of your cyber threat intelligence program and identifying your SWOT
- Reference guidance, examples and templates through the entire CTI lifecycle
- Build your CTI capabilities through:
  - Templates
  - Tools
  - Interview and competencies guides for hiring
  - Training and growth opportunities


For Health-ISAC members, if you're here remember you can find the expanded CTI in a Box with additional resources that are TLP Amber for H-ISAC only [here](https://health-isac.cyware.com/webapp/user/doc-library/76709acf-8a78-4752-b4bb-c7e5c4988983). I am the proud co-chair of the *CTI Program Development Working Group* in Health-ISAC and very excited about the amazing healthcare industry specific resources we have created there that you won't find anywhere else. We're currently working on co-authoring a whitepaper for the Health-ISAC community as well.

The folders in this project are organized by the CTI Lifecycle:



 | Link                                                         | Notes                                                        |
 | ------------------------------------------------------------ | ------------------------------------------------------------ |
 | [Planning and Direction](https://github.com/cybershujin/CTIinaBox/tree/main/1.%20Planning%20and%20Direction) | This is your getting started page, which also includes how to pitch a CTI program, how to identify your stakeholders, resources for program maturity assessments and how to document your Intelligence Requirements (IRs) and Prioritiy Intelligence Requirements (PIRs). This is a deep dive into establishing the foundation of your program, but it should be noted that the CTI lifecylce is a circle and this phase will be visted over and over again as you mature and improve your program. |
| [Collection](https://github.com/cybershujin/CTIinaBox/tree/main/2.%20Collection)            | This part of the project focuses on getting you started with data collection activities, including designing your Intelligence Collection Plan (ICP) (tied to your intelligence requirements that you worked on in the Planning and Direction phase). Additionally, this part of the project will provide you lists of open-source or very cheap sources of intelligence reports, feeds and IOCs. |
|[Processing](https://github.com/cybershujin/CTIinaBox/tree/main/3.%20Processing) | This is where you are doing to take all the data you're collecting from your Intelligence Collection Plan (ICP) and review your IRs and PIRs to understand the decisions or actions that this data is intended to support to ask yourself what additional context is needed for this data to make it relevant as an answer to your IRs and PIRs? Then you're going to review the dissemination requirements with your stakeholders to identify what format this data will need to be delivered (written report? STIX? csv files?). This will make the foundation of your Intelligence Data Processing function and will drive your selection of a Threat Intelligence Platform (TIP). Tools for analyst processing as well as open-source TIPs are provided here. Additionally templates to create use cases, RFPs, and comparison tools for threat intelligence platform selection will be kept here, in case you get budget to implement a paid service. |
| [Analysis](https://github.com/cybershujin/CTIinaBox/tree/main/4.%20Analysis) | Often an overlooked or neglected phase, analysis is the critical difference between regugitating facts and findings and true cyber threat intelligence. This section focuses on resources for training analysts, guidelines for policy and procedure implementation for your CTI program related to structured analytical techniques (SATs), as well as open-source tools for analysis. |
|[Dissemination](https://github.com/cybershujin/CTIinaBox/tree/main/5.%20Dissemination) | Many templates and guides on cyber threat intelligence products as well as guidance for documenting the IR -> ICP -> Dissemination Requirements and aligning that with your Processing Map and Feedback processes **to produce meaningful metrics** to your stakeholders.|
| [Feedback](https://github.com/cybershujin/CTIinaBox/tree/main/6.%20Feedback) | You will see in different models of the CTI lifecycle the feedback phase might be presented differently. Sometimes it is lumped together with dissemination, when the emphasis is usually placed on getting immediate and real time feedback with your stakeholders. Other times it is omitted all together, usually when the author is emphasizing that the CTI cycle is a complete circle and after dissemination your feedback should be backed into the "Planning and Direction" aspect of the lifecycle. Both are valid interpretations. I created a entirely separate section for Feedback so that this area could focus on templates and methodology for feedback, metrics, and **training for analysts**. Including training in this part of the lifecycle may seem odd at first, but truly we should be all reviewing our CTI lifecycle efforts reguarly to identify opprotunities for our teams to gain important knowledge we need to keep up with the evolving threats our organizations face.|

## There are some fantastic CTI githubs out there worth sharing.
<br>

 | Link                                                         | Notes                                                        |
 |-----------------------------| ----------------------------------------------------------------------------------------------------------------------------- |
 | [Open Source Tools for CTI by BushidoUK](https://github.com/BushidoUK/Open-source-tools-for-CTI/tree/master) | Amazing list of resources, and a fantastic CTI practioner. He breaks up his resources into strategic, tactical and operational intelligence resources. Also check out his blog too: https://bushidotoken.net and follow him on Twitter: @BushidoToken I know this reseacher from our participation in the [Curated Intel](https://curatedintel.org/) community | 
 |[Curated Itntel](https://github.com/curated-intel) | All amazing work from experts in the field. Particularly the [CTI Fundamentals](https://github.com/curated-intel/CTI-fundamentals) and the [Threat Actor Profile](https://github.com/curated-intel/Threat-Actor-Profile-Guide) repos are referenced as excellent guides in other parts of this project |
 | [A curated list of awesome Threat Intelligence resources](https://github.com/hslatman/awesome-threat-intelligence) | Includes sources, formats, frameworks and platforms, tools, research, standards and books. |
 | [Awesome Threat Intel Blogs](https://docs.google.com/spreadsheets/d/11ebsrFeCaoSup9V3n01tGw4h8vmlVhyQz0kn2EVHM-M/edit?gid=0#gid=0) | blog and feed links |
 | [Awesome Threat Intel RSS Feeds](https://github.com/thehappydinoa/awesome-threat-intel-rss) | A curated list of blogs posting threat intel. | 
 | [Free Threat Intel / IOC Feeds](https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds) | This repository contains Open Source freely usable Threat Intel feeds that can be used without additional requirements.  The CSV [ThreatIntelFeeds](https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds/blob/main/ThreatIntelFeeds.csv) is stored in a structured manner based on the Vendor, Description, Category and URL. |
 |[Ransomwatch Github](https://github.com/joshhighet/ransomwatch) and [Ransomwatch Live Site](https://ransomwatch.telemetry.ltd/#/) | providing crawling of ransomware data leak sites and victim listings, including full onion links |
 |[Ransomare.live](https://www.ransomware.live/#/) | providing crawling of ransomware data leak sites and victim listings, including full onion links |
 
 

### Contributors

I have had so many people be incredibly generous with their time and knowledge to help make this project come to life. 
|Contributor | Links | Notes |
|--------------------- | ------------------------- | --------|
| John Doyle | [Linkedin](https://www.linkedin.com/in/john-doyle-a02bab10/) | John found out I was working on this project and shared dozens of links and resources I sprinkled throughout this project. |

