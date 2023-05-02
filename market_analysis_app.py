import streamlit as st
from market_analysis import fig, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13, fig14, fig15, fig16, fig17, fig18

st.set_page_config(page_title='PANPAN & WAFI', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

with st.sidebar:

    st.subheader('MARKET ANALYSIS')
    st.markdown('<div style="text-align: left-align;">This dashboard provide insights into customer preferences for two products, '
           'PAN-PAN and WAFI-SAN, across four criteria: price, quality, choice, and convenience. '
            'The dashboard utilizes interactive visualizations to allow executives to explore and analyze '
            'the survey data, enabling businesses to make data-driven decisions to improve their '
            'product offerings and better meet customer needs. Additionally, the dashboard provides ' 
            'a user-friendly interface for easy access and interpretation of the survey results.</div>', unsafe_allow_html=True)

    st.markdown('---')

    product = st.radio(
        "Choose the product to be analyzed:",
        ('PAN-PAN', 'WAFI-SAN'))
    
    criteria = st.radio(
        "Choose a Criterion:",
        ('Price', 'Quality', 'Choice', 'Convenience'))

    st.markdown('---')

    st.caption('— John Paul M. Curada')

st.title(f'{product} {criteria} Analysis')

st.write('***Note: Click the arrow at the top-left side of the app to change the product and criterion. Also, Change the theme to dark theme for better visuals.***')
st.markdown('---')

if product == 'PAN-PAN' and criteria == 'Price':
    st.plotly_chart(fig)
    st.markdown('Insights:')
    st.markdown('- The most popular price range for PAN-PAN products is between ₱20 to ₱30, followed by ₱30 to ₱40.')
    st.markdown('- The number of respondents who prefer PAN-PAN products in the ₱30 to ₱40 range decreased significantly from grade 7 to grade 9, but increased again in grade 10 and 11.')
    st.markdown('- There is a low number of respondents who prefer PAN-PAN products in the ₱40 to ₱50 range across all grades.')
    st.markdown('Recommendations:')
    st.markdown('- PAN-PAN should continue to focus on the ₱20 to ₱30 price range, as it is the most popular among the respondents.')
    st.markdown('- There is an opportunity to increase popularity among grade 9 students by creating products that cater to the ₱30 to ₱40 price range.')
    st.markdown('- PAN-PAN should also consider discontinuing products that fall under the ₱40 to ₱50 range as it has low demand across all grades.')
    st.markdown('- Conducting further research on the reasons behind the low demand for products in the ₱40 to ₱50 range would help in determining the appropriate actions to take.')
if product == 'PAN-PAN' and criteria == 'Quality':
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('Insights:')
    st.markdown('- The most preferred serving size for PAN-PAN pancakes is 2, with grades 9 and 12 having the least preference for this serving size.')
    st.markdown('- Grades 7 to 11 have relatively consistent preferences for pancake servings, with grade 12 having a slightly lower preference for 2 and a higher preference for 1 and 3 servings.')
    st.markdown('Recommendations:')
    st.markdown('- PAN-PAN should continue to offer pancakes in serving sizes of 2, as it is the most preferred among the respondents across all grades.')
    st.markdown('- For grades 9 and 12, PAN-PAN should consider offering promotions or deals that would encourage them to try the 2-serving size pancakes.')
    st.markdown('- PAN-PAN should conduct further research on the reasons behind the low preference for 2-serving size pancakes among grades 9 and 12 to help determine the appropriate actions to take.')

    st.plotly_chart(fig2)
    st.markdown('Insights:')
    st.markdown('- Overall, paper cone is slightly less preferred than paper plate among all grades.')
    st.markdown('- There is a slight decrease in preference for paper cone from grade 7 to grade 9, but it remains relatively consistent from grade 9 to grade 12.')
    st.markdown('- Preference for paper plate fluctuates among grades, with the highest preference in grade 11.')
    st.markdown('Recommendations:')
    st.markdown('- While paper plate is more preferred, PAN-PAN should consider offering both packaging types to cater to different preferences.')
    st.markdown('- PAN-PAN can conduct further research on the reasons behind the fluctuation in preference for paper plate among different grades to identify opportunities to increase preference across all grades.')
    st.markdown('- Since preference for paper cone decreases from grade 7 to grade 9, PAN-PAN can consider introducing new packaging options for this age group to better cater to their preferences.')

    st.plotly_chart(fig3)
    st.markdown('Insights:')
    st.markdown('- Both milk and fruit juice are equally preferred among the respondents, with an average score of 5 across all grades.')
    st.markdown('- Grade 10 students have a slightly higher preference for milk compared to other grades.')
    st.markdown('- Grade 11 students have a slightly lower preference for milk compared to other grades.')
    st.markdown('Recommendations:')
    st.markdown('- As milk and fruit juice are equally preferred, PAN-PAN can consider offering both options to cater to different preferences of their customers.')
    st.markdown('- As grade 10 students have a slightly higher preference for milk, PAN-PAN can consider offering more milk-based drinks or promotions targeting this age group.')
    st.markdown('- To address the slightly lower preference for milk among grade 11 students, PAN-PAN can consider offering additional drink options or promotions targeting this age group to increase their interest in milk-based drinks.')

if product == 'PAN-PAN' and criteria == 'Choice':
    st.plotly_chart(fig4)
    st.markdown('Insights:')
    st.markdown('- Mango is the most preferred topping across all grade levels, with the highest score in Grade 12.')
    st.markdown('- Banana is the second most preferred topping in Grades 8, 9, 10, and 11. However, in Grade 7 and Grade 12, it is less preferred than Sweetened Apple.')
    st.markdown('- Sweetened Apple is the third most preferred topping in Grades 7, 8, and 9. However, in Grades 10, 11, and 12, it is less preferred than Banana.')
    st.markdown('- Random fruit is the least preferred topping across all grade levels, with the lowest score in Grades 9 and 12.')
    st.markdown('Recommendations:')
    st.markdown('- Based on these insights, PAN-PAN may want to consider offering mango as a topping option for pancakes as it is the most preferred topping among all grades. In addition, they may want to offer banana and sweetened apple as additional options, as they are also popular choices among most grades. However, offering random fruit may not be necessary as it is the least preferred topping across all grades.')

    st.plotly_chart(fig5)
    st.markdown('Insights:')
    st.markdown('- The most preferred alternative sweetener among all grade levels is maple syrup, with an average rating of 6.0.')
    st.markdown('- Honey is the second most preferred alternative sweetener, but it is preferred less compared to maple syrup, with an average rating of 3.8.')
    st.markdown('- Fruit puree is the least preferred alternative sweetener among all grade levels, with an average rating of 0.5.')
    st.markdown('Recommendations:')
    st.markdown('- It is recommended for PAN-PAN to use maple syrup as the alternative sweetener for their pancakes. However, they can also consider using honey as a second option. PAN-PAN can also consider adding more options for alternative sweeteners to cater to different preferences of their customers. They can explore using other types of sweeteners such as agave syrup or stevia.')

    st.plotly_chart(fig6)
    st.markdown('Insights:')
    st.markdown('- Based on the given data, we can see that the preferred portion size of pancake is quite consistent across all grade levels, with normal-sized pancake being the most preferred option. However, we can see a slight dip in Grade 9, where mini pancake is the least preferred option.')
    st.markdown('Recommendations:')
    st.markdown('PAN-PAN can consider offering both mini and normal-sized pancakes on their menu to cater to different preferences. However, they may want to consider promoting the normal-sized pancake more heavily as it appears to be the more popular option overall. Additionally, they can consider introducing new pancake flavors or toppings to keep their menu interesting and varied for customers.')

if product == 'PAN-PAN' and criteria == 'Convenience':
    st.plotly_chart(fig7)
    st.markdown('Insights:')
    st.markdown('- Across all grade levels, more respondents prefer to have their pancakes "To go" than "For here".')
    st.markdown('Recommendations:')
    st.markdown('Since more respondents prefer to have their pancakes "To go," PAN-PAN could consider offering more options for takeout or delivery, such as through a mobile app or online ordering platform.')
    st.markdown('To cater to the varying preferences across different grade levels, PAN-PAN could also consider offering different packaging options for takeout or delivery, depending on the convenience preferences of the customers.')
    st.markdown('PAN-PAN could also offer more incentives or promotions for customers who choose to dine in, especially for Grade 8 respondents who have the highest preference for this option.')

    st.plotly_chart(fig8)
    
if product == 'WAFI-SAN' and criteria == 'Price':
    st.plotly_chart(fig9)

if product == 'WAFI-SAN' and criteria == 'Quality':
    st.plotly_chart(fig10)
    st.plotly_chart(fig11)

if product == 'WAFI-SAN' and criteria == 'Choice':
    st.plotly_chart(fig12)
    st.plotly_chart(fig13)
    st.plotly_chart(fig14)
    st.plotly_chart(fig15)
    st.plotly_chart(fig16)

if product == 'WAFI-SAN' and criteria == 'Convenience':
    st.plotly_chart(fig17)
    st.plotly_chart(fig18)
