results = { '192.168.1.2': ('CVE-2016-8743', '2.2.32'),
            '192.168.1.12': ('CVE-2018-1283', '2.4.0'),
            '192.168.1.200': ('CVE-2022-23943', '2.4.52'),
            '192.168.1.5': ('CVE-2016-5387', '2.4.23')}

print(sorted(results.items(), key=lambda x: x[1][1]))
