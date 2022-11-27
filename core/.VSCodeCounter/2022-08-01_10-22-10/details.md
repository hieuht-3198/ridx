# Details

Date : 2022-08-01 10:22:10

Directory /home/hsnt/Documents/Docker/RiDX/core

Total : 842 files,  67334 codes, 2993 comments, 5290 blanks, all 75617 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [server/app/__init__.py](/server/app/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/config/__init__.py](/server/app/config/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/config/auth.py](/server/app/config/auth.py) | Python | 19 | 0 | 8 | 27 |
| [server/app/config/database.py](/server/app/config/database.py) | Python | 5 | 0 | 4 | 9 |
| [server/app/config/env.py](/server/app/config/env.py) | Python | 12 | 0 | 5 | 17 |
| [server/app/config/http_status.py](/server/app/config/http_status.py) | Python | 15 | 0 | 5 | 20 |
| [server/app/handle/__init__.py](/server/app/handle/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/handle/error_message.py](/server/app/handle/error_message.py) | Python | 17 | 0 | 3 | 20 |
| [server/app/handle/exception.py](/server/app/handle/exception.py) | Python | 24 | 0 | 6 | 30 |
| [server/app/helper/__init__.py](/server/app/helper/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/helper/base.py](/server/app/helper/base.py) | Python | 89 | 0 | 16 | 105 |
| [server/app/helper/cpe.py](/server/app/helper/cpe.py) | Python | 44 | 2 | 14 | 60 |
| [server/app/model/__init__.py](/server/app/model/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/model/asset.py](/server/app/model/asset.py) | Python | 37 | 7 | 19 | 63 |
| [server/app/model/auth.py](/server/app/model/auth.py) | Python | 8 | 0 | 4 | 12 |
| [server/app/model/base.py](/server/app/model/base.py) | Python | 18 | 0 | 7 | 25 |
| [server/app/model/countermeasure.py](/server/app/model/countermeasure.py) | Python | 22 | 2 | 11 | 35 |
| [server/app/model/cpe.py](/server/app/model/cpe.py) | Python | 6 | 0 | 4 | 10 |
| [server/app/model/cve.py](/server/app/model/cve.py) | Python | 8 | 7 | 4 | 19 |
| [server/app/model/cwe.py](/server/app/model/cwe.py) | Python | 8 | 0 | 3 | 11 |
| [server/app/model/deployment_scenario.py](/server/app/model/deployment_scenario.py) | Python | 115 | 0 | 39 | 154 |
| [server/app/model/risk_assessment.py](/server/app/model/risk_assessment.py) | Python | 10 | 0 | 6 | 16 |
| [server/app/model/risk_monitoring.py](/server/app/model/risk_monitoring.py) | Python | 16 | 0 | 7 | 23 |
| [server/app/model/system_profile.py](/server/app/model/system_profile.py) | Python | 14 | 0 | 8 | 22 |
| [server/app/model/user.py](/server/app/model/user.py) | Python | 13 | 0 | 7 | 20 |
| [server/app/repository/__init__.py](/server/app/repository/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/repository/assets.py](/server/app/repository/assets.py) | Python | 21 | 0 | 8 | 29 |
| [server/app/repository/auth.py](/server/app/repository/auth.py) | Python | 12 | 0 | 3 | 15 |
| [server/app/repository/base.py](/server/app/repository/base.py) | Python | 67 | 0 | 8 | 75 |
| [server/app/repository/countermeasure.py](/server/app/repository/countermeasure.py) | Python | 21 | 0 | 8 | 29 |
| [server/app/repository/cpe.py](/server/app/repository/cpe.py) | Python | 20 | 0 | 8 | 28 |
| [server/app/repository/cves.py](/server/app/repository/cves.py) | Python | 13 | 0 | 6 | 19 |
| [server/app/repository/cwes.py](/server/app/repository/cwes.py) | Python | 13 | 0 | 5 | 18 |
| [server/app/repository/deployment_scenario.py](/server/app/repository/deployment_scenario.py) | Python | 55 | 1 | 16 | 72 |
| [server/app/repository/risk_assessment.py](/server/app/repository/risk_assessment.py) | Python | 23 | 0 | 9 | 32 |
| [server/app/repository/risk_monitoring.py](/server/app/repository/risk_monitoring.py) | Python | 23 | 0 | 9 | 32 |
| [server/app/repository/system_profile.py](/server/app/repository/system_profile.py) | Python | 21 | 0 | 8 | 29 |
| [server/app/repository/user.py](/server/app/repository/user.py) | Python | 32 | 0 | 10 | 42 |
| [server/app/router/__init__.py](/server/app/router/__init__.py) | Python | 13 | 0 | 0 | 13 |
| [server/app/router/admin.py](/server/app/router/admin.py) | Python | 36 | 0 | 8 | 44 |
| [server/app/router/assessments.py](/server/app/router/assessments.py) | Python | 81 | 1 | 10 | 92 |
| [server/app/router/asset.py](/server/app/router/asset.py) | Python | 85 | 0 | 15 | 100 |
| [server/app/router/auth.py](/server/app/router/auth.py) | Python | 73 | 0 | 15 | 88 |
| [server/app/router/base.py](/server/app/router/base.py) | Python | 66 | 0 | 15 | 81 |
| [server/app/router/countermeasure.py](/server/app/router/countermeasure.py) | Python | 54 | 0 | 11 | 65 |
| [server/app/router/cpe.py](/server/app/router/cpe.py) | Python | 32 | 0 | 7 | 39 |
| [server/app/router/cves.py](/server/app/router/cves.py) | Python | 25 | 0 | 7 | 32 |
| [server/app/router/cwes.py](/server/app/router/cwes.py) | Python | 25 | 0 | 7 | 32 |
| [server/app/router/deployment_scenario.py](/server/app/router/deployment_scenario.py) | Python | 829 | 14 | 130 | 973 |
| [server/app/router/helper.py](/server/app/router/helper.py) | Python | 18 | 0 | 3 | 21 |
| [server/app/router/risk_assessment.py](/server/app/router/risk_assessment.py) | Python | 70 | 0 | 18 | 88 |
| [server/app/router/risk_monitoring.py](/server/app/router/risk_monitoring.py) | Python | 165 | 0 | 30 | 195 |
| [server/app/router/system_profile.py](/server/app/router/system_profile.py) | Python | 103 | 0 | 23 | 126 |
| [server/app/router/test_roter.py](/server/app/router/test_roter.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/services/__init__.py](/server/app/services/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/app/services/cve.py](/server/app/services/cve.py) | Python | 45 | 0 | 4 | 49 |
| [server/app/services/graph.py](/server/app/services/graph.py) | Python | 53 | 0 | 12 | 65 |
| [server/app/services/nvd.py](/server/app/services/nvd.py) | Python | 9 | 0 | 6 | 15 |
| [server/core/__init__.py](/server/core/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/attack_graph/__init__.py](/server/core/attack_graph/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/attack_graph/main.py](/server/core/attack_graph/main.py) | Python | 127 | 33 | 24 | 184 |
| [server/core/attack_graph/model/__init__.py](/server/core/attack_graph/model/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/attack_graph/model/attack_vector.py](/server/core/attack_graph/model/attack_vector.py) | Python | 7 | 0 | 5 | 12 |
| [server/core/attack_graph/model/node.py](/server/core/attack_graph/model/node.py) | Python | 28 | 0 | 17 | 45 |
| [server/core/attack_graph/model/privilege.py](/server/core/attack_graph/model/privilege.py) | Python | 7 | 0 | 5 | 12 |
| [server/core/attack_graph/model/vulnerability.py](/server/core/attack_graph/model/vulnerability.py) | Python | 12 | 0 | 5 | 17 |
| [server/core/attack_graph/sample.json](/server/core/attack_graph/sample.json) | JSON | 1,895 | 0 | 1 | 1,896 |
| [server/core/attack_graph/utils/__init__.py](/server/core/attack_graph/utils/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/attack_graph/utils/helper.py](/server/core/attack_graph/utils/helper.py) | Python | 4 | 0 | 5 | 9 |
| [server/core/bayes/__init__.py](/server/core/bayes/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/bayes/helper/__init__.py](/server/core/bayes/helper/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/bayes/helper/hepler.py](/server/core/bayes/helper/hepler.py) | Python | 18 | 1 | 4 | 23 |
| [server/core/bayes/main.py](/server/core/bayes/main.py) | Python | 136 | 0 | 1 | 137 |
| [server/core/bayes/model/__init__.py](/server/core/bayes/model/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/bayes/model/inetwork.py](/server/core/bayes/model/inetwork.py) | Python | 544 | 24 | 68 | 636 |
| [server/core/bayes/model/network.py](/server/core/bayes/model/network.py) | Python | 262 | 25 | 39 | 326 |
| [server/core/bayes/model/node.py](/server/core/bayes/model/node.py) | Python | 70 | 1 | 18 | 89 |
| [server/core/bayes/requirements.txt](/server/core/bayes/requirements.txt) | pip requirements | 24 | 0 | 1 | 25 |
| [server/core/bayes/sample_data.json](/server/core/bayes/sample_data.json) | JSON | 1 | 0 | 0 | 1 |
| [server/core/bayes/t.py](/server/core/bayes/t.py) | Python | 0 | 147 | 42 | 189 |
| [server/core/bayes/test.py](/server/core/bayes/test.py) | Python | 95 | 0 | 31 | 126 |
| [server/core/bayes/test_2.py](/server/core/bayes/test_2.py) | Python | 6 | 2 | 5 | 13 |
| [server/core/crawl/__init__.py](/server/core/crawl/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/default/__init__.py](/server/core/crawl/default/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/default/cpe.json](/server/core/crawl/default/cpe.json) | JSON | 1 | 0 | 0 | 1 |
| [server/core/crawl/default/cwes.json](/server/core/crawl/default/cwes.json) | JSON | 776 | 0 | 0 | 776 |
| [server/core/crawl/src/Untitled-1.ipynb](/server/core/crawl/src/Untitled-1.ipynb) | JSON | 227 | 0 | 1 | 228 |
| [server/core/crawl/src/__init__.py](/server/core/crawl/src/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/hepler/__init__.py](/server/core/crawl/src/hepler/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/hepler/io.py](/server/core/crawl/src/hepler/io.py) | Python | 9 | 0 | 3 | 12 |
| [server/core/crawl/src/hepler/parser_helper.py](/server/core/crawl/src/hepler/parser_helper.py) | Python | 35 | 0 | 13 | 48 |
| [server/core/crawl/src/hepler/unzip_helper.py](/server/core/crawl/src/hepler/unzip_helper.py) | Python | 4 | 0 | 1 | 5 |
| [server/core/crawl/src/import_data.py](/server/core/crawl/src/import_data.py) | Python | 85 | 11 | 14 | 110 |
| [server/core/crawl/src/main.py](/server/core/crawl/src/main.py) | Python | 146 | 4 | 19 | 169 |
| [server/core/crawl/src/model/__init__.py](/server/core/crawl/src/model/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/model/cpe.py](/server/core/crawl/src/model/cpe.py) | Python | 150 | 23 | 29 | 202 |
| [server/core/crawl/src/model/cve.py](/server/core/crawl/src/model/cve.py) | Python | 52 | 0 | 20 | 72 |
| [server/core/crawl/src/model/cwe.py](/server/core/crawl/src/model/cwe.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/parser/__init__.py](/server/core/crawl/src/parser/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/parser/cpe.py](/server/core/crawl/src/parser/cpe.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/parser/cve.py](/server/core/crawl/src/parser/cve.py) | Python | 352 | 21 | 46 | 419 |
| [server/core/crawl/src/parser/priv.py](/server/core/crawl/src/parser/priv.py) | Python | 257 | 13 | 30 | 300 |
| [server/core/crawl/src/pretreatment/__init__.py](/server/core/crawl/src/pretreatment/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/core/crawl/src/pretreatment/download.py](/server/core/crawl/src/pretreatment/download.py) | Python | 45 | 0 | 14 | 59 |
| [server/core/crawl/src/pretreatment/unzip.py](/server/core/crawl/src/pretreatment/unzip.py) | Python | 30 | 0 | 7 | 37 |
| [server/cve.ipynb](/server/cve.ipynb) | JSON | 69 | 0 | 1 | 70 |
| [server/entity.sh](/server/entity.sh) | Shell Script | 6 | 1 | 0 | 7 |
| [server/main.py](/server/main.py) | Python | 138 | 6 | 26 | 170 |
| [server/requirements.txt](/server/requirements.txt) | pip requirements | 34 | 0 | 1 | 35 |
| [server/scenarios/__init__.py](/server/scenarios/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [server/scenarios/sample_data.json](/server/scenarios/sample_data.json) | JSON | 803 | 0 | 0 | 803 |
| [server/scenarios/scenario_1.json](/server/scenarios/scenario_1.json) | JSON | 130 | 0 | 0 | 130 |
| [server/scenarios/scenario_2.json](/server/scenarios/scenario_2.json) | JSON | 130 | 0 | 0 | 130 |
| [server/test.json](/server/test.json) | JSON | 597 | 0 | 0 | 597 |
| [server/test.py](/server/test.py) | Python | 12 | 0 | 2 | 14 |
| [web/.eslintrc.js](/web/.eslintrc.js) | JavaScript | 8 | 0 | 1 | 9 |
| [web/.prettierrc.js](/web/.prettierrc.js) | JavaScript | 4 | 0 | 2 | 6 |
| [web/.stylelintrc.js](/web/.stylelintrc.js) | JavaScript | 4 | 0 | 2 | 6 |
| [web/README.md](/web/README.md) | Markdown | 36 | 0 | 22 | 58 |
| [web/config/config.dev.js](/web/config/config.dev.js) | JavaScript | 11 | 3 | 1 | 15 |
| [web/config/config.js](/web/config/config.js) | JavaScript | 50 | 22 | 1 | 73 |
| [web/config/defaultSettings.js](/web/config/defaultSettings.js) | JavaScript | 14 | 0 | 3 | 17 |
| [web/config/oneapi.json](/web/config/oneapi.json) | JSON | 593 | 0 | 1 | 594 |
| [web/config/proxy.js](/web/config/proxy.js) | JavaScript | 29 | 8 | 1 | 38 |
| [web/config/routes.js](/web/config/routes.js) | JavaScript | 169 | 40 | 1 | 210 |
| [web/dist/136.6dd0be76.async.js](/web/dist/136.6dd0be76.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/181.28f34203.async.js](/web/dist/181.28f34203.async.js) | JavaScript | 72 | 36 | 1 | 109 |
| [web/dist/210.b1096dbc.async.js](/web/dist/210.b1096dbc.async.js) | JavaScript | 3 | 0 | 1 | 4 |
| [web/dist/356.8760706c.async.js](/web/dist/356.8760706c.async.js) | JavaScript | 54 | 36 | 1 | 91 |
| [web/dist/396.75446139.async.js](/web/dist/396.75446139.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/529.30841822.chunk.css](/web/dist/529.30841822.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/529.4d2dd6b1.async.js](/web/dist/529.4d2dd6b1.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/532.776d6455.async.js](/web/dist/532.776d6455.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/568.7cf136b9.async.js](/web/dist/568.7cf136b9.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/594.bfe69094.async.js](/web/dist/594.bfe69094.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/594.e0179a0a.chunk.css](/web/dist/594.e0179a0a.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/670.1898572c.async.js](/web/dist/670.1898572c.async.js) | JavaScript | 11 | 0 | 1 | 12 |
| [web/dist/670.c9da5a50.chunk.css](/web/dist/670.c9da5a50.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/742.ac1dad8a.async.js](/web/dist/742.ac1dad8a.async.js) | JavaScript | 2 | 0 | 1 | 3 |
| [web/dist/756.664d70bb.async.js](/web/dist/756.664d70bb.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/77.d97aceac.async.js](/web/dist/77.d97aceac.async.js) | JavaScript | 2 | 5 | 1 | 8 |
| [web/dist/771.1cd5583e.async.js](/web/dist/771.1cd5583e.async.js) | JavaScript | 3 | 12 | 1 | 16 |
| [web/dist/798.3d035fef.chunk.css](/web/dist/798.3d035fef.chunk.css) | CSS | 2 | 0 | 0 | 2 |
| [web/dist/799.8f6a8fef.async.js](/web/dist/799.8f6a8fef.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/822.cdd9467d.async.js](/web/dist/822.cdd9467d.async.js) | JavaScript | 25 | 12 | 1 | 38 |
| [web/dist/831.455627f0.async.js](/web/dist/831.455627f0.async.js) | JavaScript | 2 | 0 | 1 | 3 |
| [web/dist/831.605f018e.chunk.css](/web/dist/831.605f018e.chunk.css) | CSS | 2 | 0 | 0 | 2 |
| [web/dist/87.57840d21.async.js](/web/dist/87.57840d21.async.js) | JavaScript | 45 | 7 | 2 | 54 |
| [web/dist/87.d85a5e28.chunk.css](/web/dist/87.d85a5e28.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/905.69e3f7c7.chunk.css](/web/dist/905.69e3f7c7.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/905.84e1c0d4.async.js](/web/dist/905.84e1c0d4.async.js) | JavaScript | 23 | 0 | 1 | 24 |
| [web/dist/929.b9095415.chunk.css](/web/dist/929.b9095415.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/986.975c1e4b.chunk.css](/web/dist/986.975c1e4b.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/986.eab589a3.async.js](/web/dist/986.eab589a3.async.js) | JavaScript | 6 | 4 | 1 | 11 |
| [web/dist/admin/users/index.html](/web/dist/admin/users/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/asset-manifest.json](/web/dist/asset-manifest.json) | JSON | 83 | 0 | 0 | 83 |
| [web/dist/assets/index.html](/web/dist/assets/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/countermeasures/index.html](/web/dist/countermeasures/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/dashboard/index.html](/web/dist/dashboard/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/cpe/index.html](/web/dist/data/cpe/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/cve/:id/index.html](/web/dist/data/cve/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/cve/index.html](/web/dist/data/cve/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/cwe/:id/index.html](/web/dist/data/cwe/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/cwe/index.html](/web/dist/data/cwe/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/index.html](/web/dist/data/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/data/parameters/index.html](/web/dist/data/parameters/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/deployment-scenarios/:id/index.html](/web/dist/deployment-scenarios/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/deployment-scenarios/index.html](/web/dist/deployment-scenarios/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/deployment-scenarios/mapping/:id/index.html](/web/dist/deployment-scenarios/mapping/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/index.html](/web/dist/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/logo.svg](/web/dist/logo.svg) | XML | 1 | 0 | 0 | 1 |
| [web/dist/p__404.5ef57da3.async.js](/web/dist/p__404.5ef57da3.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__404.b88066b1.chunk.css](/web/dist/p__404.b88066b1.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__admin__users.dffe325b.async.js](/web/dist/p__admin__users.dffe325b.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__assets__list.81596d47.chunk.css](/web/dist/p__assets__list.81596d47.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__assets__list.a7d5d403.async.js](/web/dist/p__assets__list.a7d5d403.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__countermeasures__list.81596d47.chunk.css](/web/dist/p__countermeasures__list.81596d47.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__countermeasures__list.a5d1f6a6.async.js](/web/dist/p__countermeasures__list.a5d1f6a6.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__dashboard__analysis.276d0ee6.chunk.css](/web/dist/p__dashboard__analysis.276d0ee6.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__dashboard__analysis.bd98c123.async.js](/web/dist/p__dashboard__analysis.bd98c123.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cpe.513c663e.async.js](/web/dist/p__data__cpe.513c663e.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cve.a40d3c4c.async.js](/web/dist/p__data__cve.a40d3c4c.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cve__$id.571e43ea.async.js](/web/dist/p__data__cve__$id.571e43ea.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cwe.546b1e9a.async.js](/web/dist/p__data__cwe.546b1e9a.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cwe__$id.b8b1da57.async.js](/web/dist/p__data__cwe__$id.b8b1da57.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__data__cwe__$id.e36e5301.chunk.css](/web/dist/p__data__cwe__$id.e36e5301.chunk.css) | CSS | 2 | 0 | 0 | 2 |
| [web/dist/p__data__parameters.01d55e38.async.js](/web/dist/p__data__parameters.01d55e38.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__deployment-scenarios.3521dbe1.chunk.css](/web/dist/p__deployment-scenarios.3521dbe1.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__deployment-scenarios.5d969fc3.async.js](/web/dist/p__deployment-scenarios.5d969fc3.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__deployment-scenarios__$id.01101d6c.chunk.css](/web/dist/p__deployment-scenarios__$id.01101d6c.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__deployment-scenarios__$id.563573dc.async.js](/web/dist/p__deployment-scenarios__$id.563573dc.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__deployment-scenarios__mapping__$id.908e10fc.chunk.css](/web/dist/p__deployment-scenarios__mapping__$id.908e10fc.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__deployment-scenarios__mapping__$id.bdc9af1c.async.js](/web/dist/p__deployment-scenarios__mapping__$id.bdc9af1c.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__risk-assessments.b277ba5c.async.js](/web/dist/p__risk-assessments.b277ba5c.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__risk-assessments__$id.49798fd0.async.js](/web/dist/p__risk-assessments__$id.49798fd0.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__risk-assessments__$id.fce926a9.chunk.css](/web/dist/p__risk-assessments__$id.fce926a9.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__risk-assessments__assessments__$id.cad5386c.chunk.css](/web/dist/p__risk-assessments__assessments__$id.cad5386c.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__risk-assessments__assessments__$id.f6b795a4.async.js](/web/dist/p__risk-assessments__assessments__$id.f6b795a4.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__risk-monitoring.86d097cf.async.js](/web/dist/p__risk-monitoring.86d097cf.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__risk-monitoring__monitoring__$id.740ba1b2.chunk.css](/web/dist/p__risk-monitoring__monitoring__$id.740ba1b2.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__risk-monitoring__monitoring__$id.98a23e0e.async.js](/web/dist/p__risk-monitoring__monitoring__$id.98a23e0e.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__system-profiles__$id.0b4d6518.async.js](/web/dist/p__system-profiles__$id.0b4d6518.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__system-profiles__$id.8649f604.chunk.css](/web/dist/p__system-profiles__$id.8649f604.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__system-profiles__list.81596d47.chunk.css](/web/dist/p__system-profiles__list.81596d47.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__system-profiles__list.f7c1c197.async.js](/web/dist/p__system-profiles__list.f7c1c197.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__user__Login.792da6eb.chunk.css](/web/dist/p__user__Login.792da6eb.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__user__Login.9b24fb50.async.js](/web/dist/p__user__Login.9b24fb50.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__user__register-result.34ba54c3.chunk.css](/web/dist/p__user__register-result.34ba54c3.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__user__register-result.6b56ea97.async.js](/web/dist/p__user__register-result.6b56ea97.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/p__user__register.a05c3180.chunk.css](/web/dist/p__user__register.a05c3180.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/p__user__register.c9b58420.async.js](/web/dist/p__user__register.c9b58420.async.js) | JavaScript | 1 | 0 | 1 | 2 |
| [web/dist/pro_icon.svg](/web/dist/pro_icon.svg) | XML | 5 | 0 | 0 | 5 |
| [web/dist/risk-assessments/:id/index.html](/web/dist/risk-assessments/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/risk-assessments/assessments/:id/index.html](/web/dist/risk-assessments/assessments/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/risk-assessments/index.html](/web/dist/risk-assessments/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/risk-monitoring/index.html](/web/dist/risk-monitoring/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/risk-monitoring/monitoring/:id/index.html](/web/dist/risk-monitoring/monitoring/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/system-profiles/:id/index.html](/web/dist/system-profiles/:id/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/system-profiles/index.html](/web/dist/system-profiles/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/t__plugin-layout__Layout.5102830f.chunk.css](/web/dist/t__plugin-layout__Layout.5102830f.chunk.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/t__plugin-layout__Layout.d17d774c.async.js](/web/dist/t__plugin-layout__Layout.d17d774c.async.js) | JavaScript | 4 | 4 | 0 | 8 |
| [web/dist/umi.022bf776.js](/web/dist/umi.022bf776.js) | JavaScript | 168 | 48 | 20 | 236 |
| [web/dist/umi.889c7afe.css](/web/dist/umi.889c7afe.css) | CSS | 1 | 0 | 0 | 1 |
| [web/dist/user/index.html](/web/dist/user/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/user/login/index.html](/web/dist/user/login/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/user/register-result/index.html](/web/dist/user/register-result/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/dist/user/register/index.html](/web/dist/user/register/index.html) | HTML | 192 | 36 | 17 | 245 |
| [web/jest.config.js](/web/jest.config.js) | JavaScript | 10 | 0 | 1 | 11 |
| [web/jsconfig.json](/web/jsconfig.json) | JSON with Comments | 7 | 4 | 0 | 11 |
| [web/mock/listTableList.js](/web/mock/listTableList.js) | JavaScript | 148 | 2 | 29 | 179 |
| [web/mock/notices.js](/web/mock/notices.js) | JavaScript | 104 | 0 | 2 | 106 |
| [web/mock/route.js](/web/mock/route.js) | JavaScript | 7 | 0 | 1 | 8 |
| [web/mock/user.js](/web/mock/user.js) | JavaScript | 202 | 9 | 10 | 221 |
| [web/package.json](/web/package.json) | JSON | 40 | 89 | 0 | 129 |
| [web/public/logo.svg](/web/public/logo.svg) | XML | 1 | 0 | 0 | 1 |
| [web/public/pro_icon.svg](/web/public/pro_icon.svg) | XML | 5 | 0 | 0 | 5 |
| [web/src/access.js](/web/src/access.js) | JavaScript | 8 | 3 | 1 | 12 |
| [web/src/app.jsx](/web/src/app.jsx) | JavaScript React | 47 | 6 | 7 | 60 |
| [web/src/components/CVSSServerity/index.jsx](/web/src/components/CVSSServerity/index.jsx) | JavaScript React | 18 | 0 | 3 | 21 |
| [web/src/components/CustomField/index.jsx](/web/src/components/CustomField/index.jsx) | JavaScript React | 25 | 0 | 4 | 29 |
| [web/src/components/CustomField/style.less](/web/src/components/CustomField/style.less) | Less | 58 | 0 | 8 | 66 |
| [web/src/components/Dashboard/Charts/Bar/index.jsx](/web/src/components/Dashboard/Charts/Bar/index.jsx) | JavaScript React | 114 | 0 | 11 | 125 |
| [web/src/components/Dashboard/Charts/ChartCard/index.jsx](/web/src/components/Dashboard/Charts/ChartCard/index.jsx) | JavaScript React | 91 | 0 | 12 | 103 |
| [web/src/components/Dashboard/Charts/ChartCard/index.less](/web/src/components/Dashboard/Charts/ChartCard/index.less) | Less | 74 | 0 | 2 | 76 |
| [web/src/components/Dashboard/Charts/Field/index.jsx](/web/src/components/Dashboard/Charts/Field/index.jsx) | JavaScript React | 9 | 0 | 3 | 12 |
| [web/src/components/Dashboard/Charts/Field/index.less](/web/src/components/Dashboard/Charts/Field/index.less) | Less | 16 | 0 | 2 | 18 |
| [web/src/components/Dashboard/Charts/Gauge/index.jsx](/web/src/components/Dashboard/Charts/Gauge/index.jsx) | JavaScript React | 161 | 0 | 11 | 172 |
| [web/src/components/Dashboard/Charts/MiniArea/index.jsx](/web/src/components/Dashboard/Charts/MiniArea/index.jsx) | JavaScript React | 110 | 0 | 3 | 113 |
| [web/src/components/Dashboard/Charts/MiniBar/index.jsx](/web/src/components/Dashboard/Charts/MiniBar/index.jsx) | JavaScript React | 40 | 0 | 4 | 44 |
| [web/src/components/Dashboard/Charts/MiniProgress/index.jsx](/web/src/components/Dashboard/Charts/MiniProgress/index.jsx) | JavaScript React | 43 | 0 | 3 | 46 |
| [web/src/components/Dashboard/Charts/Pie/index.jsx](/web/src/components/Dashboard/Charts/Pie/index.jsx) | JavaScript React | 241 | 4 | 26 | 271 |
| [web/src/components/Dashboard/Charts/TagCloud/index.jsx](/web/src/components/Dashboard/Charts/TagCloud/index.jsx) | JavaScript React | 165 | 5 | 20 | 190 |
| [web/src/components/Dashboard/Charts/TimelineChart/index.jsx](/web/src/components/Dashboard/Charts/TimelineChart/index.jsx) | JavaScript React | 127 | 2 | 8 | 137 |
| [web/src/components/Dashboard/Charts/WaterWave/index.jsx](/web/src/components/Dashboard/Charts/WaterWave/index.jsx) | JavaScript React | 207 | 4 | 35 | 246 |
| [web/src/components/Dashboard/Charts/autoHeight.jsx](/web/src/components/Dashboard/Charts/autoHeight.jsx) | JavaScript React | 62 | 0 | 14 | 76 |
| [web/src/components/Dashboard/Charts/index.jsx](/web/src/components/Dashboard/Charts/index.jsx) | JavaScript React | 10 | 0 | 3 | 13 |
| [web/src/components/Dashboard/Charts/index.less](/web/src/components/Dashboard/Charts/index.less) | Less | 19 | 0 | 1 | 20 |
| [web/src/components/Dashboard/Metric/index.jsx](/web/src/components/Dashboard/Metric/index.jsx) | JavaScript React | 53 | 0 | 1 | 54 |
| [web/src/components/Dashboard/Metric/index.less](/web/src/components/Dashboard/Metric/index.less) | Less | 4 | 0 | 0 | 4 |
| [web/src/components/Dashboard/NumberInfo/index.jsx](/web/src/components/Dashboard/NumberInfo/index.jsx) | JavaScript React | 48 | 0 | 3 | 51 |
| [web/src/components/Dashboard/NumberInfo/index.less](/web/src/components/Dashboard/NumberInfo/index.less) | Less | 67 | 0 | 2 | 69 |
| [web/src/components/Dashboard/PageLoading/index.jsx](/web/src/components/Dashboard/PageLoading/index.jsx) | JavaScript React | 11 | 1 | 2 | 14 |
| [web/src/components/Dashboard/Trend/index.jsx](/web/src/components/Dashboard/Trend/index.jsx) | JavaScript React | 25 | 0 | 3 | 28 |
| [web/src/components/Dashboard/Trend/index.less](/web/src/components/Dashboard/Trend/index.less) | Less | 33 | 0 | 5 | 38 |
| [web/src/components/Footer/index.jsx](/web/src/components/Footer/index.jsx) | JavaScript React | 7 | 0 | 1 | 8 |
| [web/src/components/HeaderDropdown/index.jsx](/web/src/components/HeaderDropdown/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/components/HeaderDropdown/index.less](/web/src/components/HeaderDropdown/index.less) | Less | 14 | 0 | 3 | 17 |
| [web/src/components/HeaderSearch/index.jsx](/web/src/components/HeaderSearch/index.jsx) | JavaScript React | 80 | 0 | 4 | 84 |
| [web/src/components/HeaderSearch/index.less](/web/src/components/HeaderSearch/index.less) | Less | 23 | 0 | 3 | 26 |
| [web/src/components/Modal/ConfirmModal.jsx](/web/src/components/Modal/ConfirmModal.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/components/NoticeIcon/NoticeIcon.jsx](/web/src/components/NoticeIcon/NoticeIcon.jsx) | JavaScript React | 106 | 0 | 9 | 115 |
| [web/src/components/NoticeIcon/NoticeList.jsx](/web/src/components/NoticeIcon/NoticeList.jsx) | JavaScript React | 93 | 0 | 5 | 98 |
| [web/src/components/NoticeIcon/NoticeList.less](/web/src/components/NoticeIcon/NoticeList.less) | Less | 96 | 0 | 8 | 104 |
| [web/src/components/NoticeIcon/index.jsx](/web/src/components/NoticeIcon/index.jsx) | JavaScript React | 130 | 0 | 19 | 149 |
| [web/src/components/NoticeIcon/index.less](/web/src/components/NoticeIcon/index.less) | Less | 30 | 0 | 6 | 36 |
| [web/src/components/RightContent/AvatarDropdown.jsx](/web/src/components/RightContent/AvatarDropdown.jsx) | JavaScript React | 68 | 17 | 12 | 97 |
| [web/src/components/RightContent/index.jsx](/web/src/components/RightContent/index.jsx) | JavaScript React | 22 | 14 | 7 | 43 |
| [web/src/components/RightContent/index.less](/web/src/components/RightContent/index.less) | Less | 79 | 0 | 6 | 85 |
| [web/src/components/TableAction/index.jsx](/web/src/components/TableAction/index.jsx) | JavaScript React | 43 | 0 | 7 | 50 |
| [web/src/components/index.md](/web/src/components/index.md) | Markdown | 242 | 0 | 31 | 273 |
| [web/src/e2e/baseLayout.e2e.js](/web/src/e2e/baseLayout.e2e.js) | JavaScript | 54 | 0 | 8 | 62 |
| [web/src/global.jsx](/web/src/global.jsx) | JavaScript React | 81 | 5 | 12 | 98 |
| [web/src/global.less](/web/src/global.less) | Less | 51 | 6 | 10 | 67 |
| [web/src/locales/en-US.js](/web/src/locales/en-US.js) | JavaScript | 26 | 0 | 1 | 27 |
| [web/src/locales/en-US/component.js](/web/src/locales/en-US/component.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/locales/en-US/custom.js](/web/src/locales/en-US/custom.js) | JavaScript | 14 | 0 | 4 | 18 |
| [web/src/locales/en-US/globalHeader.js](/web/src/locales/en-US/globalHeader.js) | JavaScript | 17 | 0 | 1 | 18 |
| [web/src/locales/en-US/menu.js](/web/src/locales/en-US/menu.js) | JavaScript | 68 | 0 | 11 | 79 |
| [web/src/locales/en-US/pages.js](/web/src/locales/en-US/pages.js) | JavaScript | 70 | 0 | 1 | 71 |
| [web/src/locales/en-US/pwa.js](/web/src/locales/en-US/pwa.js) | JavaScript | 6 | 0 | 1 | 7 |
| [web/src/locales/en-US/settingDrawer.js](/web/src/locales/en-US/settingDrawer.js) | JavaScript | 31 | 0 | 1 | 32 |
| [web/src/locales/en-US/settings.js](/web/src/locales/en-US/settings.js) | JavaScript | 60 | 0 | 1 | 61 |
| [web/src/manifest.json](/web/src/manifest.json) | JSON | 22 | 0 | 1 | 23 |
| [web/src/pages/403.jsx](/web/src/pages/403.jsx) | JavaScript React | 17 | 0 | 1 | 18 |
| [web/src/pages/404.jsx](/web/src/pages/404.jsx) | JavaScript React | 16 | 0 | 3 | 19 |
| [web/src/pages/500.jsx](/web/src/pages/500.jsx) | JavaScript React | 17 | 0 | 1 | 18 |
| [web/src/pages/Admin.jsx](/web/src/pages/Admin.jsx) | JavaScript React | 44 | 0 | 1 | 45 |
| [web/src/pages/TableList/components/UpdateForm.jsx](/web/src/pages/TableList/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/TableList/index.jsx](/web/src/pages/TableList/index.jsx) | JavaScript React | 295 | 29 | 20 | 344 |
| [web/src/pages/Welcome.jsx](/web/src/pages/Welcome.jsx) | JavaScript React | 56 | 0 | 3 | 59 |
| [web/src/pages/Welcome.less](/web/src/pages/Welcome.less) | Less | 7 | 0 | 2 | 9 |
| [web/src/pages/account/center/Center.less](/web/src/pages/account/center/Center.less) | Less | 74 | 0 | 13 | 87 |
| [web/src/pages/account/center/_mock.js](/web/src/pages/account/center/_mock.js) | JavaScript | 222 | 2 | 8 | 232 |
| [web/src/pages/account/center/components/Applications/index.jsx](/web/src/pages/account/center/components/Applications/index.jsx) | JavaScript React | 123 | 1 | 7 | 131 |
| [web/src/pages/account/center/components/Applications/index.less](/web/src/pages/account/center/components/Applications/index.less) | Less | 48 | 1 | 3 | 52 |
| [web/src/pages/account/center/components/ArticleListContent/index.jsx](/web/src/pages/account/center/components/ArticleListContent/index.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/pages/account/center/components/ArticleListContent/index.less](/web/src/pages/account/center/components/ArticleListContent/index.less) | Less | 36 | 0 | 3 | 39 |
| [web/src/pages/account/center/components/Articles/index.jsx](/web/src/pages/account/center/components/Articles/index.jsx) | JavaScript React | 55 | 0 | 4 | 59 |
| [web/src/pages/account/center/components/Articles/index.less](/web/src/pages/account/center/components/Articles/index.less) | Less | 11 | 0 | 2 | 13 |
| [web/src/pages/account/center/components/AvatarList/index.jsx](/web/src/pages/account/center/components/AvatarList/index.jsx) | JavaScript React | 55 | 0 | 7 | 62 |
| [web/src/pages/account/center/components/AvatarList/index.less](/web/src/pages/account/center/components/AvatarList/index.less) | Less | 44 | 0 | 7 | 51 |
| [web/src/pages/account/center/components/Projects/index.jsx](/web/src/pages/account/center/components/Projects/index.jsx) | JavaScript React | 52 | 1 | 3 | 56 |
| [web/src/pages/account/center/components/Projects/index.less](/web/src/pages/account/center/components/Projects/index.less) | Less | 50 | 0 | 5 | 55 |
| [web/src/pages/account/center/index.jsx](/web/src/pages/account/center/index.jsx) | JavaScript React | 246 | 1 | 18 | 265 |
| [web/src/pages/account/center/service.js](/web/src/pages/account/center/service.js) | JavaScript | 9 | 0 | 1 | 10 |
| [web/src/pages/account/settings/_mock.js](/web/src/pages/account/settings/_mock.js) | JavaScript | 71 | 2 | 6 | 79 |
| [web/src/pages/account/settings/components/BaseView.less](/web/src/pages/account/settings/components/BaseView.less) | Less | 59 | 0 | 7 | 66 |
| [web/src/pages/account/settings/components/PhoneView.jsx](/web/src/pages/account/settings/components/PhoneView.jsx) | JavaScript React | 33 | 0 | 5 | 38 |
| [web/src/pages/account/settings/components/base.jsx](/web/src/pages/account/settings/components/base.jsx) | JavaScript React | 225 | 0 | 14 | 239 |
| [web/src/pages/account/settings/components/binding.jsx](/web/src/pages/account/settings/components/binding.jsx) | JavaScript React | 43 | 0 | 4 | 47 |
| [web/src/pages/account/settings/components/notification.jsx](/web/src/pages/account/settings/components/notification.jsx) | JavaScript React | 39 | 0 | 4 | 43 |
| [web/src/pages/account/settings/components/security.jsx](/web/src/pages/account/settings/components/security.jsx) | JavaScript React | 56 | 0 | 4 | 60 |
| [web/src/pages/account/settings/geographic/city.json](/web/src/pages/account/settings/geographic/city.json) | JSON | 1,784 | 0 | 1 | 1,785 |
| [web/src/pages/account/settings/geographic/province.json](/web/src/pages/account/settings/geographic/province.json) | JSON | 138 | 0 | 1 | 139 |
| [web/src/pages/account/settings/index.jsx](/web/src/pages/account/settings/index.jsx) | JavaScript React | 94 | 0 | 18 | 112 |
| [web/src/pages/account/settings/service.js](/web/src/pages/account/settings/service.js) | JavaScript | 13 | 0 | 1 | 14 |
| [web/src/pages/account/settings/style.less](/web/src/pages/account/settings/style.less) | Less | 88 | 2 | 4 | 94 |
| [web/src/pages/admin/users/index.jsx](/web/src/pages/admin/users/index.jsx) | JavaScript React | 124 | 0 | 8 | 132 |
| [web/src/pages/admin/users/service.js](/web/src/pages/admin/users/service.js) | JavaScript | 28 | 2 | 6 | 36 |
| [web/src/pages/api-docs/index.jsx](/web/src/pages/api-docs/index.jsx) | JavaScript React | 8 | 0 | 4 | 12 |
| [web/src/pages/assets/dashboard/_mock.js](/web/src/pages/assets/dashboard/_mock.js) | JavaScript | 195 | 1 | 15 | 211 |
| [web/src/pages/assets/dashboard/components/IntroduceRow.jsx](/web/src/pages/assets/dashboard/components/IntroduceRow.jsx) | JavaScript React | 145 | 0 | 4 | 149 |
| [web/src/pages/assets/dashboard/components/OfflineData.jsx](/web/src/pages/assets/dashboard/components/OfflineData.jsx) | JavaScript React | 74 | 0 | 5 | 79 |
| [web/src/pages/assets/dashboard/components/ProportionSales.jsx](/web/src/pages/assets/dashboard/components/ProportionSales.jsx) | JavaScript React | 42 | 22 | 3 | 67 |
| [web/src/pages/assets/dashboard/components/SalesCard.jsx](/web/src/pages/assets/dashboard/components/SalesCard.jsx) | JavaScript React | 181 | 0 | 4 | 185 |
| [web/src/pages/assets/dashboard/components/TopSearch.jsx](/web/src/pages/assets/dashboard/components/TopSearch.jsx) | JavaScript React | 126 | 0 | 3 | 129 |
| [web/src/pages/assets/dashboard/index.jsx](/web/src/pages/assets/dashboard/index.jsx) | JavaScript React | 1,028 | 0 | 20 | 1,048 |
| [web/src/pages/assets/dashboard/service.js](/web/src/pages/assets/dashboard/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/assets/dashboard/style.less](/web/src/pages/assets/dashboard/style.less) | Less | 175 | 0 | 15 | 190 |
| [web/src/pages/assets/dashboard/utils/Yuan.jsx](/web/src/pages/assets/dashboard/utils/Yuan.jsx) | JavaScript React | 26 | 1 | 7 | 34 |
| [web/src/pages/assets/dashboard/utils/utils.js](/web/src/pages/assets/dashboard/utils/utils.js) | JavaScript | 39 | 0 | 8 | 47 |
| [web/src/pages/assets/dashboard/utils/utils.less](/web/src/pages/assets/dashboard/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/assets/list/_mock.js](/web/src/pages/assets/list/_mock.js) | JavaScript | 0 | 0 | 1 | 1 |
| [web/src/pages/assets/list/components/CreateForm.jsx](/web/src/pages/assets/list/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/assets/list/components/UpdateForm.jsx](/web/src/pages/assets/list/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/assets/list/index.jsx](/web/src/pages/assets/list/index.jsx) | JavaScript React | 179 | 7 | 15 | 201 |
| [web/src/pages/assets/list/index.less](/web/src/pages/assets/list/index.less) | Less | 3 | 0 | 1 | 4 |
| [web/src/pages/assets/list/service.js](/web/src/pages/assets/list/service.js) | JavaScript | 28 | 2 | 6 | 36 |
| [web/src/pages/assets/pre-lits/_mock.js](/web/src/pages/assets/pre-lits/_mock.js) | JavaScript | 30 | 0 | 5 | 35 |
| [web/src/pages/assets/pre-lits/components/CreateForm.jsx](/web/src/pages/assets/pre-lits/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/assets/pre-lits/components/UpdateForm.jsx](/web/src/pages/assets/pre-lits/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/assets/pre-lits/cwes.json](/web/src/pages/assets/pre-lits/cwes.json) | JSON | 904 | 0 | 0 | 904 |
| [web/src/pages/assets/pre-lits/index.jsx](/web/src/pages/assets/pre-lits/index.jsx) | JavaScript React | 131 | 1 | 5 | 137 |
| [web/src/pages/assets/pre-lits/service.js](/web/src/pages/assets/pre-lits/service.js) | JavaScript | 15 | 2 | 5 | 22 |
| [web/src/pages/countermeasures/dashboard/_mock.js](/web/src/pages/countermeasures/dashboard/_mock.js) | JavaScript | 195 | 1 | 15 | 211 |
| [web/src/pages/countermeasures/dashboard/components/IntroduceRow.jsx](/web/src/pages/countermeasures/dashboard/components/IntroduceRow.jsx) | JavaScript React | 145 | 0 | 4 | 149 |
| [web/src/pages/countermeasures/dashboard/components/OfflineData.jsx](/web/src/pages/countermeasures/dashboard/components/OfflineData.jsx) | JavaScript React | 74 | 0 | 5 | 79 |
| [web/src/pages/countermeasures/dashboard/components/ProportionSales.jsx](/web/src/pages/countermeasures/dashboard/components/ProportionSales.jsx) | JavaScript React | 42 | 22 | 3 | 67 |
| [web/src/pages/countermeasures/dashboard/components/SalesCard.jsx](/web/src/pages/countermeasures/dashboard/components/SalesCard.jsx) | JavaScript React | 181 | 0 | 4 | 185 |
| [web/src/pages/countermeasures/dashboard/components/TopSearch.jsx](/web/src/pages/countermeasures/dashboard/components/TopSearch.jsx) | JavaScript React | 126 | 0 | 3 | 129 |
| [web/src/pages/countermeasures/dashboard/index.jsx](/web/src/pages/countermeasures/dashboard/index.jsx) | JavaScript React | 1,028 | 0 | 20 | 1,048 |
| [web/src/pages/countermeasures/dashboard/service.js](/web/src/pages/countermeasures/dashboard/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/countermeasures/dashboard/style.less](/web/src/pages/countermeasures/dashboard/style.less) | Less | 175 | 0 | 15 | 190 |
| [web/src/pages/countermeasures/dashboard/utils/Yuan.jsx](/web/src/pages/countermeasures/dashboard/utils/Yuan.jsx) | JavaScript React | 26 | 1 | 7 | 34 |
| [web/src/pages/countermeasures/dashboard/utils/utils.js](/web/src/pages/countermeasures/dashboard/utils/utils.js) | JavaScript | 39 | 0 | 8 | 47 |
| [web/src/pages/countermeasures/dashboard/utils/utils.less](/web/src/pages/countermeasures/dashboard/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/countermeasures/list/_mock.js](/web/src/pages/countermeasures/list/_mock.js) | JavaScript | 0 | 0 | 1 | 1 |
| [web/src/pages/countermeasures/list/components/CreateForm.jsx](/web/src/pages/countermeasures/list/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/countermeasures/list/components/UpdateForm.jsx](/web/src/pages/countermeasures/list/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/countermeasures/list/index.jsx](/web/src/pages/countermeasures/list/index.jsx) | JavaScript React | 181 | 2 | 14 | 197 |
| [web/src/pages/countermeasures/list/index.less](/web/src/pages/countermeasures/list/index.less) | Less | 3 | 0 | 1 | 4 |
| [web/src/pages/countermeasures/list/service.js](/web/src/pages/countermeasures/list/service.js) | JavaScript | 28 | 2 | 6 | 36 |
| [web/src/pages/dashboard/analysis/_mock.js](/web/src/pages/dashboard/analysis/_mock.js) | JavaScript | 195 | 1 | 15 | 211 |
| [web/src/pages/dashboard/analysis/components/IntroduceRow.jsx](/web/src/pages/dashboard/analysis/components/IntroduceRow.jsx) | JavaScript React | 102 | 18 | 4 | 124 |
| [web/src/pages/dashboard/analysis/components/OfflineData.jsx](/web/src/pages/dashboard/analysis/components/OfflineData.jsx) | JavaScript React | 98 | 7 | 6 | 111 |
| [web/src/pages/dashboard/analysis/components/ProportionSales.jsx](/web/src/pages/dashboard/analysis/components/ProportionSales.jsx) | JavaScript React | 42 | 22 | 3 | 67 |
| [web/src/pages/dashboard/analysis/components/SalesCard.jsx](/web/src/pages/dashboard/analysis/components/SalesCard.jsx) | JavaScript React | 124 | 57 | 5 | 186 |
| [web/src/pages/dashboard/analysis/components/TopSearch.jsx](/web/src/pages/dashboard/analysis/components/TopSearch.jsx) | JavaScript React | 126 | 0 | 3 | 129 |
| [web/src/pages/dashboard/analysis/index.jsx](/web/src/pages/dashboard/analysis/index.jsx) | JavaScript React | 98 | 28 | 19 | 145 |
| [web/src/pages/dashboard/analysis/sample.json](/web/src/pages/dashboard/analysis/sample.json) | JSON | 909 | 0 | 0 | 909 |
| [web/src/pages/dashboard/analysis/service.js](/web/src/pages/dashboard/analysis/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/dashboard/analysis/style.less](/web/src/pages/dashboard/analysis/style.less) | Less | 175 | 0 | 15 | 190 |
| [web/src/pages/dashboard/analysis/utils/Yuan.jsx](/web/src/pages/dashboard/analysis/utils/Yuan.jsx) | JavaScript React | 26 | 1 | 7 | 34 |
| [web/src/pages/dashboard/analysis/utils/utils.js](/web/src/pages/dashboard/analysis/utils/utils.js) | JavaScript | 39 | 0 | 8 | 47 |
| [web/src/pages/dashboard/analysis/utils/utils.less](/web/src/pages/dashboard/analysis/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/dashboard/monitor/_mock.js](/web/src/pages/dashboard/monitor/_mock.js) | JavaScript | 17 | 0 | 3 | 20 |
| [web/src/pages/dashboard/monitor/components/ActiveChart/index.jsx](/web/src/pages/dashboard/monitor/components/ActiveChart/index.jsx) | JavaScript React | 83 | 0 | 11 | 94 |
| [web/src/pages/dashboard/monitor/components/ActiveChart/index.less](/web/src/pages/dashboard/monitor/components/ActiveChart/index.less) | Less | 49 | 0 | 3 | 52 |
| [web/src/pages/dashboard/monitor/components/Charts/Gauge/index.jsx](/web/src/pages/dashboard/monitor/components/Charts/Gauge/index.jsx) | JavaScript React | 161 | 0 | 11 | 172 |
| [web/src/pages/dashboard/monitor/components/Charts/MiniArea/index.jsx](/web/src/pages/dashboard/monitor/components/Charts/MiniArea/index.jsx) | JavaScript React | 110 | 0 | 3 | 113 |
| [web/src/pages/dashboard/monitor/components/Charts/Pie/index.jsx](/web/src/pages/dashboard/monitor/components/Charts/Pie/index.jsx) | JavaScript React | 241 | 4 | 27 | 272 |
| [web/src/pages/dashboard/monitor/components/Charts/TagCloud/index.jsx](/web/src/pages/dashboard/monitor/components/Charts/TagCloud/index.jsx) | JavaScript React | 165 | 5 | 20 | 190 |
| [web/src/pages/dashboard/monitor/components/Charts/WaterWave/index.jsx](/web/src/pages/dashboard/monitor/components/Charts/WaterWave/index.jsx) | JavaScript React | 207 | 4 | 35 | 246 |
| [web/src/pages/dashboard/monitor/components/Charts/autoHeight.jsx](/web/src/pages/dashboard/monitor/components/Charts/autoHeight.jsx) | JavaScript React | 62 | 0 | 14 | 76 |
| [web/src/pages/dashboard/monitor/components/Map/index.jsx](/web/src/pages/dashboard/monitor/components/Map/index.jsx) | JavaScript React | 142 | 0 | 3 | 145 |
| [web/src/pages/dashboard/monitor/index.jsx](/web/src/pages/dashboard/monitor/index.jsx) | JavaScript React | 186 | 9 | 3 | 198 |
| [web/src/pages/dashboard/monitor/service.js](/web/src/pages/dashboard/monitor/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/dashboard/monitor/style.less](/web/src/pages/dashboard/monitor/style.less) | Less | 18 | 0 | 4 | 22 |
| [web/src/pages/dashboard/workplace/_mock.js](/web/src/pages/dashboard/workplace/_mock.js) | JavaScript | 392 | 1 | 18 | 411 |
| [web/src/pages/dashboard/workplace/components/EditableLinkGroup/index.jsx](/web/src/pages/dashboard/workplace/components/EditableLinkGroup/index.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/dashboard/workplace/components/EditableLinkGroup/index.less](/web/src/pages/dashboard/workplace/components/EditableLinkGroup/index.less) | Less | 15 | 0 | 2 | 17 |
| [web/src/pages/dashboard/workplace/components/Radar/autoHeight.jsx](/web/src/pages/dashboard/workplace/components/Radar/autoHeight.jsx) | JavaScript React | 62 | 0 | 14 | 76 |
| [web/src/pages/dashboard/workplace/components/Radar/index.jsx](/web/src/pages/dashboard/workplace/components/Radar/index.jsx) | JavaScript React | 166 | 2 | 13 | 181 |
| [web/src/pages/dashboard/workplace/index.jsx](/web/src/pages/dashboard/workplace/index.jsx) | JavaScript React | 260 | 0 | 10 | 270 |
| [web/src/pages/dashboard/workplace/service.js](/web/src/pages/dashboard/workplace/service.js) | JavaScript | 10 | 0 | 1 | 11 |
| [web/src/pages/dashboard/workplace/style.less](/web/src/pages/dashboard/workplace/style.less) | Less | 234 | 2 | 15 | 251 |
| [web/src/pages/data/cpe/_mock.js](/web/src/pages/data/cpe/_mock.js) | JavaScript | 30 | 0 | 5 | 35 |
| [web/src/pages/data/cpe/components/CreateForm.jsx](/web/src/pages/data/cpe/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/data/cpe/components/UpdateForm.jsx](/web/src/pages/data/cpe/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/data/cpe/cwes.json](/web/src/pages/data/cpe/cwes.json) | JSON | 904 | 0 | 0 | 904 |
| [web/src/pages/data/cpe/index.jsx](/web/src/pages/data/cpe/index.jsx) | JavaScript React | 48 | 2 | 5 | 55 |
| [web/src/pages/data/cpe/service.js](/web/src/pages/data/cpe/service.js) | JavaScript | 15 | 2 | 5 | 22 |
| [web/src/pages/data/cve/$id/index.jsx](/web/src/pages/data/cve/$id/index.jsx) | JavaScript React | 73 | 0 | 6 | 79 |
| [web/src/pages/data/cve/$id/service.js](/web/src/pages/data/cve/$id/service.js) | JavaScript | 8 | 2 | 4 | 14 |
| [web/src/pages/data/cve/_mock.js](/web/src/pages/data/cve/_mock.js) | JavaScript | 30 | 0 | 5 | 35 |
| [web/src/pages/data/cve/components/CreateForm.jsx](/web/src/pages/data/cve/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/data/cve/components/UpdateForm.jsx](/web/src/pages/data/cve/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/data/cve/cwes.json](/web/src/pages/data/cve/cwes.json) | JSON | 904 | 0 | 0 | 904 |
| [web/src/pages/data/cve/index.jsx](/web/src/pages/data/cve/index.jsx) | JavaScript React | 88 | 1 | 7 | 96 |
| [web/src/pages/data/cve/service.js](/web/src/pages/data/cve/service.js) | JavaScript | 15 | 2 | 5 | 22 |
| [web/src/pages/data/cwe/$id/index.jsx](/web/src/pages/data/cwe/$id/index.jsx) | JavaScript React | 60 | 0 | 6 | 66 |
| [web/src/pages/data/cwe/$id/service.js](/web/src/pages/data/cwe/$id/service.js) | JavaScript | 8 | 2 | 4 | 14 |
| [web/src/pages/data/cwe/_mock.js](/web/src/pages/data/cwe/_mock.js) | JavaScript | 30 | 0 | 5 | 35 |
| [web/src/pages/data/cwe/components/CreateForm.jsx](/web/src/pages/data/cwe/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/data/cwe/components/UpdateForm.jsx](/web/src/pages/data/cwe/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/data/cwe/cwes.json](/web/src/pages/data/cwe/cwes.json) | JSON | 904 | 0 | 0 | 904 |
| [web/src/pages/data/cwe/index.jsx](/web/src/pages/data/cwe/index.jsx) | JavaScript React | 48 | 15 | 7 | 70 |
| [web/src/pages/data/cwe/service.js](/web/src/pages/data/cwe/service.js) | JavaScript | 15 | 2 | 5 | 22 |
| [web/src/pages/data/parameters/_mock.js](/web/src/pages/data/parameters/_mock.js) | JavaScript | 30 | 0 | 5 | 35 |
| [web/src/pages/data/parameters/components/CreateForm.jsx](/web/src/pages/data/parameters/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/data/parameters/components/UpdateForm.jsx](/web/src/pages/data/parameters/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/data/parameters/cwes.json](/web/src/pages/data/parameters/cwes.json) | JSON | 904 | 0 | 0 | 904 |
| [web/src/pages/data/parameters/index.jsx](/web/src/pages/data/parameters/index.jsx) | JavaScript React | 47 | 15 | 8 | 70 |
| [web/src/pages/data/parameters/service.js](/web/src/pages/data/parameters/service.js) | JavaScript | 15 | 2 | 5 | 22 |
| [web/src/pages/deployment-scenarios/$id/components/IntroduceRow.jsx](/web/src/pages/deployment-scenarios/$id/components/IntroduceRow.jsx) | JavaScript React | 257 | 100 | 9 | 366 |
| [web/src/pages/deployment-scenarios/$id/components/Rank.jsx](/web/src/pages/deployment-scenarios/$id/components/Rank.jsx) | JavaScript React | 30 | 0 | 6 | 36 |
| [web/src/pages/deployment-scenarios/$id/components/RiskHeadMap.jsx](/web/src/pages/deployment-scenarios/$id/components/RiskHeadMap.jsx) | JavaScript React | 62 | 0 | 7 | 69 |
| [web/src/pages/deployment-scenarios/$id/components/RiskRating.jsx](/web/src/pages/deployment-scenarios/$id/components/RiskRating.jsx) | JavaScript React | 107 | 2 | 10 | 119 |
| [web/src/pages/deployment-scenarios/$id/components/TopAsset.jsx](/web/src/pages/deployment-scenarios/$id/components/TopAsset.jsx) | JavaScript React | 12 | 0 | 5 | 17 |
| [web/src/pages/deployment-scenarios/$id/components/TopRiskAssessment.jsx](/web/src/pages/deployment-scenarios/$id/components/TopRiskAssessment.jsx) | JavaScript React | 12 | 0 | 5 | 17 |
| [web/src/pages/deployment-scenarios/$id/components/TopVulnerability.jsx](/web/src/pages/deployment-scenarios/$id/components/TopVulnerability.jsx) | JavaScript React | 12 | 0 | 5 | 17 |
| [web/src/pages/deployment-scenarios/$id/index.jsx](/web/src/pages/deployment-scenarios/$id/index.jsx) | JavaScript React | 193 | 2 | 14 | 209 |
| [web/src/pages/deployment-scenarios/$id/style.less](/web/src/pages/deployment-scenarios/$id/style.less) | Less | 174 | 1 | 15 | 190 |
| [web/src/pages/deployment-scenarios/components/DetailDeploymentScenario.jsx](/web/src/pages/deployment-scenarios/components/DetailDeploymentScenario.jsx) | JavaScript React | 288 | 0 | 13 | 301 |
| [web/src/pages/deployment-scenarios/components/EditDeploymentScenario.jsx](/web/src/pages/deployment-scenarios/components/EditDeploymentScenario.jsx) | JavaScript React | 49 | 0 | 4 | 53 |
| [web/src/pages/deployment-scenarios/components/ImportDeploymentScenario.jsx](/web/src/pages/deployment-scenarios/components/ImportDeploymentScenario.jsx) | JavaScript React | 301 | 0 | 13 | 314 |
| [web/src/pages/deployment-scenarios/components/MappingVul/AssetToCPE.jsx](/web/src/pages/deployment-scenarios/components/MappingVul/AssetToCPE.jsx) | JavaScript React | 234 | 14 | 18 | 266 |
| [web/src/pages/deployment-scenarios/components/MappingVul/CPEToCVE.jsx](/web/src/pages/deployment-scenarios/components/MappingVul/CPEToCVE.jsx) | JavaScript React | 149 | 0 | 15 | 164 |
| [web/src/pages/deployment-scenarios/components/MappingVul/MappingCPE.jsx](/web/src/pages/deployment-scenarios/components/MappingVul/MappingCPE.jsx) | JavaScript React | 82 | 3 | 11 | 96 |
| [web/src/pages/deployment-scenarios/components/MappingVul/index.jsx](/web/src/pages/deployment-scenarios/components/MappingVul/index.jsx) | JavaScript React | 56 | 0 | 8 | 64 |
| [web/src/pages/deployment-scenarios/components/MappingVul/index.less](/web/src/pages/deployment-scenarios/components/MappingVul/index.less) | Less | 9 | 1 | 1 | 11 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/CustomFlow.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/CustomFlow.jsx) | JavaScript React | 26 | 4 | 2 | 32 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/common/IconFont/index.js](/web/src/pages/deployment-scenarios/components/asset-relationship/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/index.less](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 171 | 13 | 17 | 201 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 12 | 12 | 3 | 27 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/index.less](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 30 | 10 | 3 | 43 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/index.less](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorMinimap/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 21 | 6 | 3 | 30 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/index.jsx) | JavaScript React | 2 | 0 | 0 | 2 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/index.less](/web/src/pages/deployment-scenarios/components/asset-relationship/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/index.jsx](/web/src/pages/deployment-scenarios/components/asset-relationship/index.jsx) | JavaScript React | 34 | 8 | 4 | 46 |
| [web/src/pages/deployment-scenarios/components/asset-relationship/index.less](/web/src/pages/deployment-scenarios/components/asset-relationship/index.less) | Less | 42 | 0 | 8 | 50 |
| [web/src/pages/deployment-scenarios/components/attacker/index.jsx](/web/src/pages/deployment-scenarios/components/attacker/index.jsx) | JavaScript React | 300 | 1 | 13 | 314 |
| [web/src/pages/deployment-scenarios/components/attacker/service.js](/web/src/pages/deployment-scenarios/components/attacker/service.js) | JavaScript | 35 | 2 | 7 | 44 |
| [web/src/pages/deployment-scenarios/components/countermeasures/index.jsx](/web/src/pages/deployment-scenarios/components/countermeasures/index.jsx) | JavaScript React | 207 | 1 | 11 | 219 |
| [web/src/pages/deployment-scenarios/components/countermeasures/service.js](/web/src/pages/deployment-scenarios/components/countermeasures/service.js) | JavaScript | 35 | 2 | 7 | 44 |
| [web/src/pages/deployment-scenarios/components/index.less](/web/src/pages/deployment-scenarios/components/index.less) | Less | 49 | 1 | 10 | 60 |
| [web/src/pages/deployment-scenarios/components/info/index.jsx](/web/src/pages/deployment-scenarios/components/info/index.jsx) | JavaScript React | 23 | 0 | 5 | 28 |
| [web/src/pages/deployment-scenarios/index.jsx](/web/src/pages/deployment-scenarios/index.jsx) | JavaScript React | 537 | 29 | 46 | 612 |
| [web/src/pages/deployment-scenarios/index.less](/web/src/pages/deployment-scenarios/index.less) | Less | 16 | 0 | 4 | 20 |
| [web/src/pages/deployment-scenarios/mapping/$id/index.jsx](/web/src/pages/deployment-scenarios/mapping/$id/index.jsx) | JavaScript React | 42 | 0 | 10 | 52 |
| [web/src/pages/deployment-scenarios/mapping/$id/index.less](/web/src/pages/deployment-scenarios/mapping/$id/index.less) | Less | 0 | 0 | 1 | 1 |
| [web/src/pages/deployment-scenarios/service.js](/web/src/pages/deployment-scenarios/service.js) | JavaScript | 91 | 2 | 17 | 110 |
| [web/src/pages/deployment-scenarios/style.css](/web/src/pages/deployment-scenarios/style.css) | CSS | 9 | 0 | 0 | 9 |
| [web/src/pages/document.ejs](/web/src/pages/document.ejs) | HTML | 182 | 36 | 16 | 234 |
| [web/src/pages/editor/flow/common/IconFont/index.js](/web/src/pages/editor/flow/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/editor/flow/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/editor/flow/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/editor/flow/components/EditorContextMenu/KoniContextMenu.jsx](/web/src/pages/editor/flow/components/EditorContextMenu/KoniContextMenu.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/flow/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/editor/flow/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/editor/flow/components/EditorContextMenu/MindContextMenu.jsx](/web/src/pages/editor/flow/components/EditorContextMenu/MindContextMenu.jsx) | JavaScript React | 19 | 0 | 3 | 22 |
| [web/src/pages/editor/flow/components/EditorContextMenu/index.jsx](/web/src/pages/editor/flow/components/EditorContextMenu/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/flow/components/EditorContextMenu/index.less](/web/src/pages/editor/flow/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/editor/flow/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 113 | 0 | 11 | 124 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/editor/flow/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 24 | 0 | 3 | 27 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/KoniDetailPanel.jsx](/web/src/pages/editor/flow/components/EditorDetailPanel/KoniDetailPanel.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/MindDetailPanel.jsx](/web/src/pages/editor/flow/components/EditorDetailPanel/MindDetailPanel.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/index.jsx](/web/src/pages/editor/flow/components/EditorDetailPanel/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/flow/components/EditorDetailPanel/index.less](/web/src/pages/editor/flow/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/editor/flow/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/editor/flow/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 50 | 0 | 3 | 53 |
| [web/src/pages/editor/flow/components/EditorItemPanel/KoniItemPanel.jsx](/web/src/pages/editor/flow/components/EditorItemPanel/KoniItemPanel.jsx) | JavaScript React | 46 | 0 | 3 | 49 |
| [web/src/pages/editor/flow/components/EditorItemPanel/index.jsx](/web/src/pages/editor/flow/components/EditorItemPanel/index.jsx) | JavaScript React | 3 | 0 | 1 | 4 |
| [web/src/pages/editor/flow/components/EditorItemPanel/index.less](/web/src/pages/editor/flow/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/editor/flow/components/EditorMinimap/index.jsx](/web/src/pages/editor/flow/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/editor/flow/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/editor/flow/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 27 | 0 | 3 | 30 |
| [web/src/pages/editor/flow/components/EditorToolbar/KoniToolbar.jsx](/web/src/pages/editor/flow/components/EditorToolbar/KoniToolbar.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/flow/components/EditorToolbar/MindToolbar.jsx](/web/src/pages/editor/flow/components/EditorToolbar/MindToolbar.jsx) | JavaScript React | 22 | 0 | 3 | 25 |
| [web/src/pages/editor/flow/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/editor/flow/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/editor/flow/components/EditorToolbar/index.jsx](/web/src/pages/editor/flow/components/EditorToolbar/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/flow/components/EditorToolbar/index.less](/web/src/pages/editor/flow/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/editor/flow/index.jsx](/web/src/pages/editor/flow/index.jsx) | JavaScript React | 34 | 0 | 1 | 35 |
| [web/src/pages/editor/flow/index.less](/web/src/pages/editor/flow/index.less) | Less | 41 | 0 | 8 | 49 |
| [web/src/pages/editor/koni/common/IconFont/index.js](/web/src/pages/editor/koni/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/editor/koni/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/editor/koni/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/editor/koni/components/EditorContextMenu/KoniContextMenu.jsx](/web/src/pages/editor/koni/components/EditorContextMenu/KoniContextMenu.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/koni/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/editor/koni/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/editor/koni/components/EditorContextMenu/MindContextMenu.jsx](/web/src/pages/editor/koni/components/EditorContextMenu/MindContextMenu.jsx) | JavaScript React | 19 | 0 | 3 | 22 |
| [web/src/pages/editor/koni/components/EditorContextMenu/index.jsx](/web/src/pages/editor/koni/components/EditorContextMenu/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/koni/components/EditorContextMenu/index.less](/web/src/pages/editor/koni/components/EditorContextMenu/index.less) | Less | 35 | 0 | 6 | 41 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/editor/koni/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 113 | 0 | 11 | 124 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/editor/koni/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 24 | 0 | 3 | 27 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/KoniDetailPanel.jsx](/web/src/pages/editor/koni/components/EditorDetailPanel/KoniDetailPanel.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/MindDetailPanel.jsx](/web/src/pages/editor/koni/components/EditorDetailPanel/MindDetailPanel.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/index.jsx](/web/src/pages/editor/koni/components/EditorDetailPanel/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/koni/components/EditorDetailPanel/index.less](/web/src/pages/editor/koni/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/editor/koni/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/editor/koni/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 50 | 0 | 3 | 53 |
| [web/src/pages/editor/koni/components/EditorItemPanel/KoniItemPanel.jsx](/web/src/pages/editor/koni/components/EditorItemPanel/KoniItemPanel.jsx) | JavaScript React | 46 | 0 | 3 | 49 |
| [web/src/pages/editor/koni/components/EditorItemPanel/index.jsx](/web/src/pages/editor/koni/components/EditorItemPanel/index.jsx) | JavaScript React | 3 | 0 | 1 | 4 |
| [web/src/pages/editor/koni/components/EditorItemPanel/index.less](/web/src/pages/editor/koni/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/editor/koni/components/EditorMinimap/index.jsx](/web/src/pages/editor/koni/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/editor/koni/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/editor/koni/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 27 | 0 | 3 | 30 |
| [web/src/pages/editor/koni/components/EditorToolbar/KoniToolbar.jsx](/web/src/pages/editor/koni/components/EditorToolbar/KoniToolbar.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/koni/components/EditorToolbar/MindToolbar.jsx](/web/src/pages/editor/koni/components/EditorToolbar/MindToolbar.jsx) | JavaScript React | 22 | 0 | 3 | 25 |
| [web/src/pages/editor/koni/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/editor/koni/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/editor/koni/components/EditorToolbar/index.jsx](/web/src/pages/editor/koni/components/EditorToolbar/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/koni/components/EditorToolbar/index.less](/web/src/pages/editor/koni/components/EditorToolbar/index.less) | Less | 34 | 0 | 6 | 40 |
| [web/src/pages/editor/koni/index.jsx](/web/src/pages/editor/koni/index.jsx) | JavaScript React | 34 | 0 | 1 | 35 |
| [web/src/pages/editor/koni/index.less](/web/src/pages/editor/koni/index.less) | Less | 48 | 0 | 9 | 57 |
| [web/src/pages/editor/mind/common/IconFont/index.js](/web/src/pages/editor/mind/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/editor/mind/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/editor/mind/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/editor/mind/components/EditorContextMenu/KoniContextMenu.jsx](/web/src/pages/editor/mind/components/EditorContextMenu/KoniContextMenu.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/mind/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/editor/mind/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/editor/mind/components/EditorContextMenu/MindContextMenu.jsx](/web/src/pages/editor/mind/components/EditorContextMenu/MindContextMenu.jsx) | JavaScript React | 19 | 0 | 3 | 22 |
| [web/src/pages/editor/mind/components/EditorContextMenu/index.jsx](/web/src/pages/editor/mind/components/EditorContextMenu/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/mind/components/EditorContextMenu/index.less](/web/src/pages/editor/mind/components/EditorContextMenu/index.less) | Less | 35 | 0 | 6 | 41 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/editor/mind/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 113 | 0 | 11 | 124 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/editor/mind/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 24 | 0 | 3 | 27 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/KoniDetailPanel.jsx](/web/src/pages/editor/mind/components/EditorDetailPanel/KoniDetailPanel.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/MindDetailPanel.jsx](/web/src/pages/editor/mind/components/EditorDetailPanel/MindDetailPanel.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/index.jsx](/web/src/pages/editor/mind/components/EditorDetailPanel/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/mind/components/EditorDetailPanel/index.less](/web/src/pages/editor/mind/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/editor/mind/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/editor/mind/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 50 | 0 | 3 | 53 |
| [web/src/pages/editor/mind/components/EditorItemPanel/KoniItemPanel.jsx](/web/src/pages/editor/mind/components/EditorItemPanel/KoniItemPanel.jsx) | JavaScript React | 46 | 0 | 3 | 49 |
| [web/src/pages/editor/mind/components/EditorItemPanel/index.jsx](/web/src/pages/editor/mind/components/EditorItemPanel/index.jsx) | JavaScript React | 3 | 0 | 1 | 4 |
| [web/src/pages/editor/mind/components/EditorItemPanel/index.less](/web/src/pages/editor/mind/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/editor/mind/components/EditorMinimap/index.jsx](/web/src/pages/editor/mind/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/editor/mind/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/editor/mind/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 27 | 0 | 3 | 30 |
| [web/src/pages/editor/mind/components/EditorToolbar/KoniToolbar.jsx](/web/src/pages/editor/mind/components/EditorToolbar/KoniToolbar.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/editor/mind/components/EditorToolbar/MindToolbar.jsx](/web/src/pages/editor/mind/components/EditorToolbar/MindToolbar.jsx) | JavaScript React | 22 | 0 | 3 | 25 |
| [web/src/pages/editor/mind/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/editor/mind/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/editor/mind/components/EditorToolbar/index.jsx](/web/src/pages/editor/mind/components/EditorToolbar/index.jsx) | JavaScript React | 4 | 0 | 1 | 5 |
| [web/src/pages/editor/mind/components/EditorToolbar/index.less](/web/src/pages/editor/mind/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/editor/mind/index.jsx](/web/src/pages/editor/mind/index.jsx) | JavaScript React | 31 | 0 | 1 | 32 |
| [web/src/pages/editor/mind/index.less](/web/src/pages/editor/mind/index.less) | Less | 48 | 0 | 9 | 57 |
| [web/src/pages/editor/mind/worldCup2018.json](/web/src/pages/editor/mind/worldCup2018.json) | JSON | 129 | 0 | 1 | 130 |
| [web/src/pages/exception/403/index.jsx](/web/src/pages/exception/403/index.jsx) | JavaScript React | 17 | 0 | 1 | 18 |
| [web/src/pages/exception/404/index.jsx](/web/src/pages/exception/404/index.jsx) | JavaScript React | 17 | 0 | 1 | 18 |
| [web/src/pages/exception/500/index.jsx](/web/src/pages/exception/500/index.jsx) | JavaScript React | 17 | 0 | 1 | 18 |
| [web/src/pages/form/advanced-form/_mock.js](/web/src/pages/form/advanced-form/_mock.js) | JavaScript | 9 | 1 | 1 | 11 |
| [web/src/pages/form/advanced-form/components/TableForm.jsx](/web/src/pages/form/advanced-form/components/TableForm.jsx) | JavaScript React | 222 | 1 | 29 | 252 |
| [web/src/pages/form/advanced-form/index.jsx](/web/src/pages/form/advanced-form/index.jsx) | JavaScript React | 500 | 1 | 14 | 515 |
| [web/src/pages/form/advanced-form/service.js](/web/src/pages/form/advanced-form/service.js) | JavaScript | 7 | 0 | 1 | 8 |
| [web/src/pages/form/advanced-form/style.less](/web/src/pages/form/advanced-form/style.less) | Less | 58 | 0 | 8 | 66 |
| [web/src/pages/form/basic-form/_mock.js](/web/src/pages/form/basic-form/_mock.js) | JavaScript | 9 | 1 | 1 | 11 |
| [web/src/pages/form/basic-form/index.jsx](/web/src/pages/form/basic-form/index.jsx) | JavaScript React | 184 | 0 | 10 | 194 |
| [web/src/pages/form/basic-form/service.js](/web/src/pages/form/basic-form/service.js) | JavaScript | 7 | 0 | 1 | 8 |
| [web/src/pages/form/basic-form/style.less](/web/src/pages/form/basic-form/style.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/form/step-form/_mock.js](/web/src/pages/form/step-form/_mock.js) | JavaScript | 9 | 1 | 1 | 11 |
| [web/src/pages/form/step-form/index.jsx](/web/src/pages/form/step-form/index.jsx) | JavaScript React | 221 | 0 | 8 | 229 |
| [web/src/pages/form/step-form/service.js](/web/src/pages/form/step-form/service.js) | JavaScript | 7 | 0 | 1 | 8 |
| [web/src/pages/form/step-form/style.less](/web/src/pages/form/step-form/style.less) | Less | 9 | 0 | 3 | 12 |
| [web/src/pages/list/basic-list/_mock.js](/web/src/pages/list/basic-list/_mock.js) | JavaScript | 140 | 2 | 15 | 157 |
| [web/src/pages/list/basic-list/components/OperationModal.jsx](/web/src/pages/list/basic-list/components/OperationModal.jsx) | JavaScript React | 117 | 0 | 5 | 122 |
| [web/src/pages/list/basic-list/index.jsx](/web/src/pages/list/basic-list/index.jsx) | JavaScript React | 232 | 0 | 15 | 247 |
| [web/src/pages/list/basic-list/service.js](/web/src/pages/list/basic-list/service.js) | JavaScript | 24 | 0 | 1 | 25 |
| [web/src/pages/list/basic-list/style.less](/web/src/pages/list/basic-list/style.less) | Less | 186 | 0 | 10 | 196 |
| [web/src/pages/list/basic-list/utils/utils.less](/web/src/pages/list/basic-list/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/list/card-list/_mock.js](/web/src/pages/list/card-list/_mock.js) | JavaScript | 104 | 1 | 6 | 111 |
| [web/src/pages/list/card-list/index.jsx](/web/src/pages/list/card-list/index.jsx) | JavaScript React | 102 | 0 | 4 | 106 |
| [web/src/pages/list/card-list/service.js](/web/src/pages/list/card-list/service.js) | JavaScript | 6 | 0 | 1 | 7 |
| [web/src/pages/list/card-list/style.less](/web/src/pages/list/card-list/style.less) | Less | 97 | 0 | 11 | 108 |
| [web/src/pages/list/card-list/utils/utils.less](/web/src/pages/list/card-list/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/list/search/applications/_mock.js](/web/src/pages/list/search/applications/_mock.js) | JavaScript | 104 | 1 | 6 | 111 |
| [web/src/pages/list/search/applications/components/StandardFormRow/index.jsx](/web/src/pages/list/search/applications/components/StandardFormRow/index.jsx) | JavaScript React | 21 | 0 | 3 | 24 |
| [web/src/pages/list/search/applications/components/StandardFormRow/index.less](/web/src/pages/list/search/applications/components/StandardFormRow/index.less) | Less | 82 | 0 | 6 | 88 |
| [web/src/pages/list/search/applications/components/TagSelect/index.jsx](/web/src/pages/list/search/applications/components/TagSelect/index.jsx) | JavaScript React | 98 | 0 | 15 | 113 |
| [web/src/pages/list/search/applications/components/TagSelect/index.less](/web/src/pages/list/search/applications/components/TagSelect/index.less) | Less | 32 | 0 | 3 | 35 |
| [web/src/pages/list/search/applications/index.jsx](/web/src/pages/list/search/applications/index.jsx) | JavaScript React | 204 | 0 | 5 | 209 |
| [web/src/pages/list/search/applications/service.js](/web/src/pages/list/search/applications/service.js) | JavaScript | 6 | 0 | 1 | 7 |
| [web/src/pages/list/search/applications/style.less](/web/src/pages/list/search/applications/style.less) | Less | 47 | 1 | 3 | 51 |
| [web/src/pages/list/search/applications/utils/utils.less](/web/src/pages/list/search/applications/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/list/search/articles/_mock.js](/web/src/pages/list/search/articles/_mock.js) | JavaScript | 104 | 1 | 6 | 111 |
| [web/src/pages/list/search/articles/components/ArticleListContent/index.jsx](/web/src/pages/list/search/articles/components/ArticleListContent/index.jsx) | JavaScript React | 15 | 0 | 3 | 18 |
| [web/src/pages/list/search/articles/components/ArticleListContent/index.less](/web/src/pages/list/search/articles/components/ArticleListContent/index.less) | Less | 36 | 0 | 3 | 39 |
| [web/src/pages/list/search/articles/components/StandardFormRow/index.jsx](/web/src/pages/list/search/articles/components/StandardFormRow/index.jsx) | JavaScript React | 21 | 0 | 3 | 24 |
| [web/src/pages/list/search/articles/components/StandardFormRow/index.less](/web/src/pages/list/search/articles/components/StandardFormRow/index.less) | Less | 84 | 0 | 5 | 89 |
| [web/src/pages/list/search/articles/components/TagSelect/index.jsx](/web/src/pages/list/search/articles/components/TagSelect/index.jsx) | JavaScript React | 98 | 0 | 15 | 113 |
| [web/src/pages/list/search/articles/components/TagSelect/index.less](/web/src/pages/list/search/articles/components/TagSelect/index.less) | Less | 32 | 0 | 2 | 34 |
| [web/src/pages/list/search/articles/index.jsx](/web/src/pages/list/search/articles/index.jsx) | JavaScript React | 258 | 0 | 10 | 268 |
| [web/src/pages/list/search/articles/service.js](/web/src/pages/list/search/articles/service.js) | JavaScript | 6 | 0 | 1 | 7 |
| [web/src/pages/list/search/articles/style.less](/web/src/pages/list/search/articles/style.less) | Less | 29 | 0 | 3 | 32 |
| [web/src/pages/list/search/index.jsx](/web/src/pages/list/search/index.jsx) | JavaScript React | 76 | 1 | 12 | 89 |
| [web/src/pages/list/search/projects/_mock.js](/web/src/pages/list/search/projects/_mock.js) | JavaScript | 104 | 0 | 6 | 110 |
| [web/src/pages/list/search/projects/components/AvatarList/index.jsx](/web/src/pages/list/search/projects/components/AvatarList/index.jsx) | JavaScript React | 55 | 0 | 7 | 62 |
| [web/src/pages/list/search/projects/components/AvatarList/index.less](/web/src/pages/list/search/projects/components/AvatarList/index.less) | Less | 44 | 0 | 7 | 51 |
| [web/src/pages/list/search/projects/components/StandardFormRow/index.jsx](/web/src/pages/list/search/projects/components/StandardFormRow/index.jsx) | JavaScript React | 21 | 0 | 3 | 24 |
| [web/src/pages/list/search/projects/components/StandardFormRow/index.less](/web/src/pages/list/search/projects/components/StandardFormRow/index.less) | Less | 84 | 0 | 5 | 89 |
| [web/src/pages/list/search/projects/components/TagSelect/index.jsx](/web/src/pages/list/search/projects/components/TagSelect/index.jsx) | JavaScript React | 98 | 0 | 15 | 113 |
| [web/src/pages/list/search/projects/components/TagSelect/index.less](/web/src/pages/list/search/projects/components/TagSelect/index.less) | Less | 32 | 0 | 2 | 34 |
| [web/src/pages/list/search/projects/index.jsx](/web/src/pages/list/search/projects/index.jsx) | JavaScript React | 150 | 2 | 4 | 156 |
| [web/src/pages/list/search/projects/service.js](/web/src/pages/list/search/projects/service.js) | JavaScript | 6 | 0 | 1 | 7 |
| [web/src/pages/list/search/projects/style.less](/web/src/pages/list/search/projects/style.less) | Less | 51 | 0 | 5 | 56 |
| [web/src/pages/list/search/projects/utils/utils.less](/web/src/pages/list/search/projects/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/list/table-list/_mock.js](/web/src/pages/list/table-list/_mock.js) | JavaScript | 153 | 3 | 31 | 187 |
| [web/src/pages/list/table-list/components/CreateForm.jsx](/web/src/pages/list/table-list/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/list/table-list/components/UpdateForm.jsx](/web/src/pages/list/table-list/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/list/table-list/index.jsx](/web/src/pages/list/table-list/index.jsx) | JavaScript React | 278 | 18 | 19 | 315 |
| [web/src/pages/list/table-list/service.js](/web/src/pages/list/table-list/service.js) | JavaScript | 29 | 6 | 6 | 41 |
| [web/src/pages/profile/advanced/_mock.js](/web/src/pages/profile/advanced/_mock.js) | JavaScript | 75 | 0 | 3 | 78 |
| [web/src/pages/profile/advanced/index.jsx](/web/src/pages/profile/advanced/index.jsx) | JavaScript React | 423 | 0 | 11 | 434 |
| [web/src/pages/profile/advanced/service.js](/web/src/pages/profile/advanced/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/profile/advanced/style.less](/web/src/pages/profile/advanced/style.less) | Less | 54 | 0 | 7 | 61 |
| [web/src/pages/profile/basic/_mock.js](/web/src/pages/profile/basic/_mock.js) | JavaScript | 87 | 0 | 3 | 90 |
| [web/src/pages/profile/basic/index.jsx](/web/src/pages/profile/basic/index.jsx) | JavaScript React | 225 | 0 | 12 | 237 |
| [web/src/pages/profile/basic/service.js](/web/src/pages/profile/basic/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/profile/basic/style.less](/web/src/pages/profile/basic/style.less) | Less | 7 | 0 | 2 | 9 |
| [web/src/pages/result/fail/index.jsx](/web/src/pages/result/fail/index.jsx) | JavaScript React | 72 | 0 | 1 | 73 |
| [web/src/pages/result/fail/index.less](/web/src/pages/result/fail/index.less) | Less | 10 | 0 | 2 | 12 |
| [web/src/pages/result/success/index.jsx](/web/src/pages/result/success/index.jsx) | JavaScript React | 131 | 0 | 1 | 132 |
| [web/src/pages/result/success/index.less](/web/src/pages/result/success/index.less) | Less | 13 | 0 | 3 | 16 |
| [web/src/pages/risk-assessments/$id/_mock.js](/web/src/pages/risk-assessments/$id/_mock.js) | JavaScript | 126 | 1 | 5 | 132 |
| [web/src/pages/risk-assessments/$id/assessment/index.jsx](/web/src/pages/risk-assessments/$id/assessment/index.jsx) | JavaScript React | 419 | 4 | 15 | 438 |
| [web/src/pages/risk-assessments/$id/attack_graph/CustomFlow.jsx](/web/src/pages/risk-assessments/$id/attack_graph/CustomFlow.jsx) | JavaScript React | 26 | 6 | 2 | 34 |
| [web/src/pages/risk-assessments/$id/attack_graph/common/IconFont/index.js](/web/src/pages/risk-assessments/$id/attack_graph/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/index.less](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 189 | 17 | 19 | 225 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 12 | 12 | 3 | 27 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/index.less](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 32 | 10 | 3 | 45 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/index.less](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorMinimap/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 13 | 14 | 3 | 30 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/index.jsx) | JavaScript React | 2 | 0 | 0 | 2 |
| [web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/index.less](/web/src/pages/risk-assessments/$id/attack_graph/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/risk-assessments/$id/attack_graph/index.jsx](/web/src/pages/risk-assessments/$id/attack_graph/index.jsx) | JavaScript React | 75 | 4 | 7 | 86 |
| [web/src/pages/risk-assessments/$id/attack_graph/index.less](/web/src/pages/risk-assessments/$id/attack_graph/index.less) | Less | 42 | 0 | 8 | 50 |
| [web/src/pages/risk-assessments/$id/attack_graph/service.js](/web/src/pages/risk-assessments/$id/attack_graph/service.js) | JavaScript | 11 | 2 | 3 | 16 |
| [web/src/pages/risk-assessments/$id/countermeasures/index.css](/web/src/pages/risk-assessments/$id/countermeasures/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/$id/countermeasures/index.jsx](/web/src/pages/risk-assessments/$id/countermeasures/index.jsx) | JavaScript React | 68 | 0 | 8 | 76 |
| [web/src/pages/risk-assessments/$id/index.jsx](/web/src/pages/risk-assessments/$id/index.jsx) | JavaScript React | 123 | 0 | 12 | 135 |
| [web/src/pages/risk-assessments/$id/index.less](/web/src/pages/risk-assessments/$id/index.less) | Less | 6 | 1 | 1 | 8 |
| [web/src/pages/risk-assessments/$id/service.js](/web/src/pages/risk-assessments/$id/service.js) | JavaScript | 8 | 2 | 3 | 13 |
| [web/src/pages/risk-assessments/$id/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx](/web/src/pages/risk-assessments/$id/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx) | JavaScript React | 76 | 0 | 8 | 84 |
| [web/src/pages/risk-assessments/$id/vulnerability-setting/components/index.css](/web/src/pages/risk-assessments/$id/vulnerability-setting/components/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/$id/vulnerability-setting/index.css](/web/src/pages/risk-assessments/$id/vulnerability-setting/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-assessments/$id/vulnerability-setting/index.jsx](/web/src/pages/risk-assessments/$id/vulnerability-setting/index.jsx) | JavaScript React | 119 | 0 | 4 | 123 |
| [web/src/pages/risk-assessments/assessments/$id/_mock.js](/web/src/pages/risk-assessments/assessments/$id/_mock.js) | JavaScript | 126 | 1 | 5 | 132 |
| [web/src/pages/risk-assessments/assessments/$id/assessment/index.jsx](/web/src/pages/risk-assessments/assessments/$id/assessment/index.jsx) | JavaScript React | 489 | 28 | 18 | 535 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/CustomFlow.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/CustomFlow.jsx) | JavaScript React | 26 | 4 | 2 | 32 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/common/IconFont/index.js](/web/src/pages/risk-assessments/assessments/$id/attack_graph/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/index.less](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 188 | 17 | 19 | 224 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 12 | 12 | 3 | 27 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/index.less](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 32 | 10 | 3 | 45 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/index.less](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorMinimap/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 21 | 6 | 3 | 30 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/index.jsx) | JavaScript React | 2 | 0 | 0 | 2 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/index.less](/web/src/pages/risk-assessments/assessments/$id/attack_graph/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/index.jsx](/web/src/pages/risk-assessments/assessments/$id/attack_graph/index.jsx) | JavaScript React | 148 | 3 | 11 | 162 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/index.less](/web/src/pages/risk-assessments/assessments/$id/attack_graph/index.less) | Less | 42 | 0 | 8 | 50 |
| [web/src/pages/risk-assessments/assessments/$id/attack_graph/service.js](/web/src/pages/risk-assessments/assessments/$id/attack_graph/service.js) | JavaScript | 11 | 2 | 3 | 16 |
| [web/src/pages/risk-assessments/assessments/$id/countermeasures/index.css](/web/src/pages/risk-assessments/assessments/$id/countermeasures/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/assessments/$id/countermeasures/index.jsx](/web/src/pages/risk-assessments/assessments/$id/countermeasures/index.jsx) | JavaScript React | 204 | 3 | 15 | 222 |
| [web/src/pages/risk-assessments/assessments/$id/index.jsx](/web/src/pages/risk-assessments/assessments/$id/index.jsx) | JavaScript React | 165 | 4 | 13 | 182 |
| [web/src/pages/risk-assessments/assessments/$id/index.less](/web/src/pages/risk-assessments/assessments/$id/index.less) | Less | 6 | 1 | 1 | 8 |
| [web/src/pages/risk-assessments/assessments/$id/service.js](/web/src/pages/risk-assessments/assessments/$id/service.js) | JavaScript | 107 | 2 | 15 | 124 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx](/web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx) | JavaScript React | 129 | 35 | 12 | 176 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/components/index.css](/web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/components/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/index.css](/web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/index.jsx](/web/src/pages/risk-assessments/assessments/$id/vulnerability-analysis/index.jsx) | JavaScript React | 91 | 0 | 8 | 99 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx](/web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx) | JavaScript React | 266 | 0 | 19 | 285 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/components/index.css](/web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/components/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/index.css](/web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/index.jsx](/web/src/pages/risk-assessments/assessments/$id/vulnerability-setting/index.jsx) | JavaScript React | 152 | 0 | 8 | 160 |
| [web/src/pages/risk-assessments/components/ImportDeploymentScenario.jsx](/web/src/pages/risk-assessments/components/ImportDeploymentScenario.jsx) | JavaScript React | 232 | 0 | 11 | 243 |
| [web/src/pages/risk-assessments/components/index.less](/web/src/pages/risk-assessments/components/index.less) | Less | 44 | 0 | 9 | 53 |
| [web/src/pages/risk-assessments/index.jsx](/web/src/pages/risk-assessments/index.jsx) | JavaScript React | 139 | 2 | 4 | 145 |
| [web/src/pages/risk-assessments/index.less](/web/src/pages/risk-assessments/index.less) | Less | 4 | 0 | 1 | 5 |
| [web/src/pages/risk-assessments/service.js](/web/src/pages/risk-assessments/service.js) | JavaScript | 29 | 2 | 6 | 37 |
| [web/src/pages/risk-assessments/style.css](/web/src/pages/risk-assessments/style.css) | CSS | 0 | 9 | 0 | 9 |
| [web/src/pages/risk-monitoring/components/ImportDeploymentScenario.jsx](/web/src/pages/risk-monitoring/components/ImportDeploymentScenario.jsx) | JavaScript React | 232 | 0 | 11 | 243 |
| [web/src/pages/risk-monitoring/components/index.less](/web/src/pages/risk-monitoring/components/index.less) | Less | 44 | 0 | 9 | 53 |
| [web/src/pages/risk-monitoring/index.jsx](/web/src/pages/risk-monitoring/index.jsx) | JavaScript React | 146 | 10 | 6 | 162 |
| [web/src/pages/risk-monitoring/index.less](/web/src/pages/risk-monitoring/index.less) | Less | 4 | 0 | 1 | 5 |
| [web/src/pages/risk-monitoring/monitoring/$id/_mock.js](/web/src/pages/risk-monitoring/monitoring/$id/_mock.js) | JavaScript | 126 | 1 | 5 | 132 |
| [web/src/pages/risk-monitoring/monitoring/$id/detect-threat/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/detect-threat/index.jsx) | JavaScript React | 58 | 0 | 9 | 67 |
| [web/src/pages/risk-monitoring/monitoring/$id/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/index.jsx) | JavaScript React | 118 | 0 | 10 | 128 |
| [web/src/pages/risk-monitoring/monitoring/$id/index.less](/web/src/pages/risk-monitoring/monitoring/$id/index.less) | Less | 6 | 1 | 1 | 8 |
| [web/src/pages/risk-monitoring/monitoring/$id/monitor/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/monitor/index.jsx) | JavaScript React | 401 | 2 | 30 | 433 |
| [web/src/pages/risk-monitoring/monitoring/$id/scan-vulnerability/$id/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/scan-vulnerability/$id/index.jsx) | JavaScript React | 100 | 10 | 7 | 117 |
| [web/src/pages/risk-monitoring/monitoring/$id/service.js](/web/src/pages/risk-monitoring/monitoring/$id/service.js) | JavaScript | 124 | 2 | 19 | 145 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/_mock.js](/web/src/pages/risk-monitoring/monitoring/$id/update/_mock.js) | JavaScript | 126 | 1 | 5 | 132 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/assessment/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/assessment/index.jsx) | JavaScript React | 467 | 28 | 18 | 513 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/CustomFlow.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/CustomFlow.jsx) | JavaScript React | 26 | 4 | 2 | 32 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/common/IconFont/index.js](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 188 | 17 | 19 | 224 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 12 | 12 | 3 | 27 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 32 | 10 | 3 | 45 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorMinimap/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 21 | 6 | 3 | 30 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/index.jsx) | JavaScript React | 2 | 0 | 0 | 2 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/index.jsx) | JavaScript React | 144 | 3 | 10 | 157 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/index.less) | Less | 42 | 0 | 8 | 50 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/service.js](/web/src/pages/risk-monitoring/monitoring/$id/update/attack_graph/service.js) | JavaScript | 11 | 2 | 3 | 16 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/countermeasures/index.css](/web/src/pages/risk-monitoring/monitoring/$id/update/countermeasures/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/countermeasures/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/countermeasures/index.jsx) | JavaScript React | 204 | 3 | 15 | 222 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/index.jsx) | JavaScript React | 150 | 4 | 13 | 167 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/index.less](/web/src/pages/risk-monitoring/monitoring/$id/update/index.less) | Less | 6 | 1 | 1 | 8 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/service.js](/web/src/pages/risk-monitoring/monitoring/$id/update/service.js) | JavaScript | 107 | 2 | 15 | 124 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx) | JavaScript React | 129 | 35 | 12 | 176 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/components/index.css](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/components/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/index.css](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-analysis/index.jsx) | JavaScript React | 91 | 0 | 8 | 99 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx) | JavaScript React | 232 | 35 | 19 | 286 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/components/index.css](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/components/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/index.css](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/index.jsx](/web/src/pages/risk-monitoring/monitoring/$id/update/vulnerability-setting/index.jsx) | JavaScript React | 87 | 0 | 8 | 95 |
| [web/src/pages/risk-monitoring/service.js](/web/src/pages/risk-monitoring/service.js) | JavaScript | 29 | 2 | 6 | 37 |
| [web/src/pages/risk-monitoring/style.css](/web/src/pages/risk-monitoring/style.css) | CSS | 0 | 9 | 0 | 9 |
| [web/src/pages/risk-monitoring/update_attack_graph/_mock.js](/web/src/pages/risk-monitoring/update_attack_graph/_mock.js) | JavaScript | 126 | 1 | 5 | 132 |
| [web/src/pages/risk-monitoring/update_attack_graph/assessment/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/assessment/index.jsx) | JavaScript React | 463 | 24 | 17 | 504 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/CustomFlow.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/CustomFlow.jsx) | JavaScript React | 26 | 4 | 2 | 32 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/common/IconFont/index.js](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/common/IconFont/index.js) | JavaScript | 5 | 0 | 1 | 6 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/FlowContextMenu.jsx) | JavaScript React | 31 | 0 | 3 | 34 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/MenuItem.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/MenuItem.jsx) | JavaScript React | 17 | 0 | 4 | 21 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/index.less](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorContextMenu/index.less) | Less | 35 | 0 | 7 | 42 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/DetailForm.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/DetailForm.jsx) | JavaScript React | 182 | 13 | 17 | 212 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/FlowDetailPanel.jsx) | JavaScript React | 12 | 12 | 3 | 27 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/index.less](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorDetailPanel/index.less) | Less | 5 | 0 | 2 | 7 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/FlowItemPanel.jsx) | JavaScript React | 20 | 20 | 3 | 43 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/index.jsx) | JavaScript React | 2 | 0 | 1 | 3 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/index.less](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorItemPanel/index.less) | Less | 17 | 0 | 3 | 20 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorMinimap/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorMinimap/index.jsx) | JavaScript React | 8 | 0 | 3 | 11 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/FlowToolbar.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/FlowToolbar.jsx) | JavaScript React | 21 | 6 | 3 | 30 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/ToolbarButton.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/ToolbarButton.jsx) | JavaScript React | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/index.jsx) | JavaScript React | 2 | 0 | 0 | 2 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/index.less](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/components/EditorToolbar/index.less) | Less | 34 | 0 | 7 | 41 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/index.jsx) | JavaScript React | 138 | 2 | 10 | 150 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/index.less](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/index.less) | Less | 42 | 0 | 8 | 50 |
| [web/src/pages/risk-monitoring/update_attack_graph/attack_graph/service.js](/web/src/pages/risk-monitoring/update_attack_graph/attack_graph/service.js) | JavaScript | 11 | 2 | 3 | 16 |
| [web/src/pages/risk-monitoring/update_attack_graph/countermeasures/index.css](/web/src/pages/risk-monitoring/update_attack_graph/countermeasures/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/update_attack_graph/countermeasures/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/countermeasures/index.jsx) | JavaScript React | 204 | 3 | 15 | 222 |
| [web/src/pages/risk-monitoring/update_attack_graph/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/index.jsx) | JavaScript React | 138 | 4 | 11 | 153 |
| [web/src/pages/risk-monitoring/update_attack_graph/index.less](/web/src/pages/risk-monitoring/update_attack_graph/index.less) | Less | 6 | 1 | 1 | 8 |
| [web/src/pages/risk-monitoring/update_attack_graph/service.js](/web/src/pages/risk-monitoring/update_attack_graph/service.js) | JavaScript | 97 | 2 | 14 | 113 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/components/VulnerabiliesAnalysisPerAsset.jsx) | JavaScript React | 124 | 0 | 14 | 138 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/components/index.css](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/components/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/index.css](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-analysis/index.jsx) | JavaScript React | 90 | 0 | 8 | 98 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/components/VulnerabiliesSettingPerAsset.jsx) | JavaScript React | 266 | 0 | 19 | 285 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/components/index.css](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/components/index.css) | CSS | 21 | 0 | 4 | 25 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/index.css](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/index.css) | CSS | 15 | 0 | 4 | 19 |
| [web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/index.jsx](/web/src/pages/risk-monitoring/update_attack_graph/vulnerability-setting/index.jsx) | JavaScript React | 87 | 0 | 8 | 95 |
| [web/src/pages/system-profiles/$id/index.jsx](/web/src/pages/system-profiles/$id/index.jsx) | JavaScript React | 66 | 5 | 10 | 81 |
| [web/src/pages/system-profiles/$id/index.less](/web/src/pages/system-profiles/$id/index.less) | Less | 3 | 0 | 1 | 4 |
| [web/src/pages/system-profiles/$id/service.js](/web/src/pages/system-profiles/$id/service.js) | JavaScript | 8 | 1 | 4 | 13 |
| [web/src/pages/system-profiles/components/IntroduceRow.jsx](/web/src/pages/system-profiles/components/IntroduceRow.jsx) | JavaScript React | 60 | 4 | 4 | 68 |
| [web/src/pages/system-profiles/components/SystemProfileTopFive.jsx](/web/src/pages/system-profiles/components/SystemProfileTopFive.jsx) | JavaScript React | 70 | 4 | 5 | 79 |
| [web/src/pages/system-profiles/components/style.less](/web/src/pages/system-profiles/components/style.less) | Less | 175 | 0 | 15 | 190 |
| [web/src/pages/system-profiles/dashboard/_mock.js](/web/src/pages/system-profiles/dashboard/_mock.js) | JavaScript | 195 | 1 | 15 | 211 |
| [web/src/pages/system-profiles/dashboard/components/IntroduceRow.jsx](/web/src/pages/system-profiles/dashboard/components/IntroduceRow.jsx) | JavaScript React | 145 | 0 | 4 | 149 |
| [web/src/pages/system-profiles/dashboard/components/OfflineData.jsx](/web/src/pages/system-profiles/dashboard/components/OfflineData.jsx) | JavaScript React | 73 | 1 | 5 | 79 |
| [web/src/pages/system-profiles/dashboard/components/ProportionSales.jsx](/web/src/pages/system-profiles/dashboard/components/ProportionSales.jsx) | JavaScript React | 42 | 22 | 3 | 67 |
| [web/src/pages/system-profiles/dashboard/components/SalesCard.jsx](/web/src/pages/system-profiles/dashboard/components/SalesCard.jsx) | JavaScript React | 124 | 57 | 5 | 186 |
| [web/src/pages/system-profiles/dashboard/components/TopSearch.jsx](/web/src/pages/system-profiles/dashboard/components/TopSearch.jsx) | JavaScript React | 126 | 0 | 3 | 129 |
| [web/src/pages/system-profiles/dashboard/index.jsx](/web/src/pages/system-profiles/dashboard/index.jsx) | JavaScript React | 1,028 | 0 | 20 | 1,048 |
| [web/src/pages/system-profiles/dashboard/service.js](/web/src/pages/system-profiles/dashboard/service.js) | JavaScript | 4 | 0 | 1 | 5 |
| [web/src/pages/system-profiles/dashboard/style.less](/web/src/pages/system-profiles/dashboard/style.less) | Less | 175 | 0 | 15 | 190 |
| [web/src/pages/system-profiles/dashboard/utils/Yuan.jsx](/web/src/pages/system-profiles/dashboard/utils/Yuan.jsx) | JavaScript React | 26 | 1 | 7 | 34 |
| [web/src/pages/system-profiles/dashboard/utils/utils.js](/web/src/pages/system-profiles/dashboard/utils/utils.js) | JavaScript | 39 | 0 | 8 | 47 |
| [web/src/pages/system-profiles/dashboard/utils/utils.less](/web/src/pages/system-profiles/dashboard/utils/utils.less) | Less | 46 | 2 | 3 | 51 |
| [web/src/pages/system-profiles/list/_mock.js](/web/src/pages/system-profiles/list/_mock.js) | JavaScript | 0 | 0 | 1 | 1 |
| [web/src/pages/system-profiles/list/components/CreateForm.jsx](/web/src/pages/system-profiles/list/components/CreateForm.jsx) | JavaScript React | 17 | 0 | 3 | 20 |
| [web/src/pages/system-profiles/list/components/UpdateForm.jsx](/web/src/pages/system-profiles/list/components/UpdateForm.jsx) | JavaScript React | 141 | 0 | 3 | 144 |
| [web/src/pages/system-profiles/list/index.jsx](/web/src/pages/system-profiles/list/index.jsx) | JavaScript React | 236 | 2 | 13 | 251 |
| [web/src/pages/system-profiles/list/index.less](/web/src/pages/system-profiles/list/index.less) | Less | 3 | 0 | 1 | 4 |
| [web/src/pages/system-profiles/list/service.js](/web/src/pages/system-profiles/list/service.js) | JavaScript | 35 | 2 | 7 | 44 |
| [web/src/pages/user/Login/index.jsx](/web/src/pages/user/Login/index.jsx) | JavaScript React | 128 | 10 | 11 | 149 |
| [web/src/pages/user/Login/index.less](/web/src/pages/user/Login/index.less) | Less | 43 | 0 | 8 | 51 |
| [web/src/pages/user/register-result/index.jsx](/web/src/pages/user/register-result/index.jsx) | JavaScript React | 33 | 0 | 3 | 36 |
| [web/src/pages/user/register-result/style.less](/web/src/pages/user/register-result/style.less) | Less | 23 | 0 | 1 | 24 |
| [web/src/pages/user/register/_mock.js](/web/src/pages/user/register/_mock.js) | JavaScript | 10 | 1 | 1 | 12 |
| [web/src/pages/user/register/index.jsx](/web/src/pages/user/register/index.jsx) | JavaScript React | 281 | 0 | 25 | 306 |
| [web/src/pages/user/register/service.js](/web/src/pages/user/register/service.js) | JavaScript | 7 | 0 | 1 | 8 |
| [web/src/pages/user/register/style.less](/web/src/pages/user/register/style.less) | Less | 49 | 0 | 12 | 61 |
| [web/src/service-worker.js](/web/src/service-worker.js) | JavaScript | 37 | 22 | 7 | 66 |
| [web/src/services/api.js](/web/src/services/api.js) | JavaScript | 98 | 13 | 15 | 126 |
| [web/src/services/index.js](/web/src/services/index.js) | JavaScript | 6 | 4 | 2 | 12 |
| [web/src/services/login.js](/web/src/services/login.js) | JavaScript | 8 | 3 | 3 | 14 |
| [web/src/shared/common.js](/web/src/shared/common.js) | JavaScript | 180 | 0 | 18 | 198 |
| [web/src/shared/constant.js](/web/src/shared/constant.js) | JavaScript | 349 | 0 | 21 | 370 |
| [web/src/shared/excel.js](/web/src/shared/excel.js) | JavaScript | 0 | 0 | 1 | 1 |
| [web/src/shared/key.js](/web/src/shared/key.js) | JavaScript | 3 | 0 | 0 | 3 |
| [web/tests/PuppeteerEnvironment.js](/web/tests/PuppeteerEnvironment.js) | JavaScript | 30 | 4 | 8 | 42 |
| [web/tests/beforeTest.js](/web/tests/beforeTest.js) | JavaScript | 29 | 6 | 5 | 40 |
| [web/tests/getBrowser.js](/web/tests/getBrowser.js) | JavaScript | 37 | 5 | 4 | 46 |
| [web/tests/run-tests.js](/web/tests/run-tests.js) | JavaScript | 37 | 8 | 6 | 51 |
| [web/tests/setupTests.js](/web/tests/setupTests.js) | JavaScript | 7 | 1 | 3 | 11 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)