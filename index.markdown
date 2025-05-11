---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: "Brazil Votes: How right came to power in 2018 and lost it in 2022"

nav:
  - title: "Overview"   # 👈 This is what appears in the upper-right
    url: /

---

A visual analysis of the race between left and right ideologies.


## **Introduction**
Between 2014 and 2022, Brazil experienced dramatic political shifts. This project investigates how geography, development, and demographics shaped the race between left- and right-wing ideologies during presidential elections. Using official voting data and socioeconomic indicators, we uncover patterns in city-level results across time and space.

## **Who Won in Each City and State?**
The interactive map below shows Brazilian municipalities colored by the vote direction (left vs. right) in each election year. Use the selector to switch between 2014, 2018, and 2022.

#### **City analysis**
<iframe
  src="elections_br.html"
  width="100%"
  height="400"
  style="border:none; margin-bottom: 40px;"
  loading="lazy">
</iframe>



## **How City Size Influenced the Vote**
Small towns tended to favor Bolsonaro (right), while larger cities leaned toward Lula (left). This division highlights how population size and urbanization correlate with political preferences.


## **State-Level Patterns**
This state-level visualization emphasizes broader geographic divisions, showing regional voting trends across Brazilian states.



#### **City Size Analysis**



## **Voting from Abroad**
Many Brazilian citizens cast their votes from abroad. This map shows which side won in each foreign city with a Brazilian polling station. 

Over time, a clear shift is visible: while right-leaning support was more prominent in 2014, many cities—especially across Latin America, Africa, and Europe—moved toward the left in 2018 and 2022. The plot highlights not only regional political shifts but also reflects how diaspora communities around the world align with evolving domestic trends in Brazil.

<img 
  src="{{ site.baseurl }}/assets/global_vote_direction.png" 
  alt="Global vote direction map"
  style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />


## **Human Development Index (HDI) and Vote Direction**
This plot reveals a strong correlation between HDI and political preference. Right-leaning municipalities consistently exhibit higher HDI scores, while left-leaning areas cluster around lower values.

<img 
  src="{{ site.baseurl }}/assets/HDI_Distribution.png" 
  alt="Global vote direction map"
  style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />

Municipalities that supported right-wing candidates tend to have better indicators in income, education, and longevity (the HDI components). This trend persisted—and even sharpened—across all three elections. The socioeconomic divide has not only endured but grown more distinct over time.

## **Demography**


The following plots shows a clear trend: municipalities with a low percentage of Black and Indigenous population tend to vote right, while those with higher minority representation lean more toward the left. Most cities have minority proportions below 20%, and in these areas, right-leaning candidates dominate the vote share.

<img 
  src="{{ site.baseurl }}/assets/minority_composition_vs_vote_share.png" 
  alt="Global vote direction map"
  style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />

<img 
  src="{{ site.baseurl }}/assets/average_minority_population.png" 
  alt="Global vote direction map"
  style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />
  
As the minority proportion increases, support for left-leaning candidates becomes more common, especially beyond the 30–40% range. This suggests a strong correlation between racial composition and political preference.

Overall, the data highlights how race and electoral outcomes are closely linked in Brazil, with minority-rich cities more aligned with left-wing candidates.

## **Social Programs**


<div style="margin-bottom: 40px;">
  <iframe
    src="elections_state.html"
    width="100%"
    height="400"
    style="border:none;"
    loading="lazy">
  </iframe>
</div>


<div style="margin-bottom: 40px;">
  <iframe
    src="bolsa_familia_map.html"
    width="100%"
    height="400"
    style="border:none;"
    loading="lazy">
  </iframe>
</div>

States in Brazil with a higher proportion of households participating in social assistance programs—as reflected in the number of families per 1,000 inhabitants—tend to be concentrated in regions that have historically shown greater support for left-leaning political parties. This correlation suggests that social policies and redistributive programs may resonate more strongly with populations in economically vulnerable states, such as Piauí, Maranhão, and Alagoas. These areas not only have higher rates of participation in programs like Bolsa Família but also consistently report higher left-wing vote shares in national elections. While correlation does not imply causation, this pattern highlights the socio-political alignment between social program beneficiaries and progressive political agendas.


## **Conclusion**
Brazil's recent presidential elections tell a story of deep and persistent divides—urban vs. rural, high vs. low HDI, north vs. south, and domestic vs. expatriate voters. These divides reflect underlying structural inequalities that continue to shape the nation's political landscape. Visualizing these patterns helps reveal just how entrenched, and global, these splits have become.

