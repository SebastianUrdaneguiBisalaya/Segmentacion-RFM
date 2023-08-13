# SEGMENTATION = {
#     r'[1-2][1-2]': 'Hibernating',
#     r'[1-2][3-4]': "At risk",
#     r'[1-2]5': "Can\'t looser",
#     r'3[1-2]': "About to sleep",
#     r'33': "Need attention",
#     r'[3-4][4-5]': "Loyal customers",
#     r'41': "Promising",
#     r'51': "New customers",
#     r'[4-5][2-3]': "Potential Loyalists",
#     r'5[4-5]': "Champions"
# }
# RFM["Segment"] = RFM["R"].astype(str) + RFM["F"].astype(str)
# RFM["Segment"] = RFM["Segment"].replace(SEGMENTATION, regex = True)