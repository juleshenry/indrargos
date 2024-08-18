import asyncio
# add this import for running in jupyter notebook
import nest_asyncio

nest_asyncio.apply()
from surrealdb import Surreal
from surreal_langchain import SurrealDBStore
from langchain.embeddings import HuggingFaceEmbeddings

async def delete_docs():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("langchain", "database")
        await db.delete("documents")

async def main():
    await delete_docs()
    embeddings = HuggingFaceEmbeddings()
    sdb = SurrealDBStore(
        dburl="ws://localhost:8000/rpc",  # url for the hosted SurrealDB database
        embedding_function=embeddings,
        db_user="root",  # SurrealDB credentials if needed: db username
        db_pass="root",  # SurrealDB credentials if needed: db password
        # ns="langchain", # namespace to use for vectorstore
        # db="database",  # database to use for vectorstore
        # collection="documents", #collection to use for vectorstore
    )
    sentences = [
    "Enoh Charges Falconets to go for U20 World Cup Glory as Team Departs for Colombia",
    "‘Difficult decision to close Brazil office', Elon Musk says if X had agreed to…",
    "Elon Musk’s X to shut operations in Brazil with immediate effect",
    "X shuts Brazil operations over 'censorship' orders: Musk",
    "Moderate mag. 4.7 earthquake - 70 km southeast of Arica, Arica, Arica and Parinacota, Chile, on Sunday, Aug 18, 2024,…",
    "X says it is closing operations in Brazil due to judge’s content order to block alleged ‘fake news’ accounts",
    "Prince Harry's Cocaine Use Resurfaces Ahead of Colombia Trip",
    "Oil Spill Reported Off Venezuela’s Caribbean Coast",
    "Bolivia bus crash kills 14, leaves 18 injured",
    "Trump blasts ‘Comrade Kamala,’ says Democrat’s economic policies will make America communist",
    "“Maduro Must Go!” Shout Venezuelans at Home and Abroad",
    "Social media platform X to shutter local operations in Brazil",
    "Sarah vine: Charles must stop these pound-shop royals trashing the Monarchy's brand",
    "X to shutter local operations in Brazil amid Musk legal battle",
    "Venezuelan opposition vows to fight 'to the end'",
    "MSC GRI - scope: USA to SAWC (South America West Coast)",
    "At the Alamo, demonstrators protest Venezuela’s disputed election",
    "Meghan Markle and Prince Harry Feel the Beat at Colombian Drum School: 'I Can Tell She's Excited,' Says Founder",
    "X to End Operations in Brazil Over ‘Censorship Orders’",
    "Meet the people whose hearts age more slowly",
    "Gallery: Protesters gather in Bayfront Park rally against election fraud in Venezuela",
    "How Duchess Meghan Styles a Flowy Summer Set",
    "Protests across Venezuela as election dispute goes on",
    "X Shuts Down Operations In Large Country After Supreme Court Justice Allegedly Threatens Arrest",
    "Lip Reader Reveals What Meghan Markle Commanded Prince Harry to Do on Camera During Colombia…",
    "Pro-opposition Venezuelans protest election 'fraud'",
    "Grapevine August 18, 2024: Preserving and promoting Yiddish",
    "‘Effective immediately’: X shuts down operations in Brazil citing arrest ‘threat’",
    "Prince Harry and Meghan Markle tour bombshells - dad dancing, awkward greeting and bullet shield",
    "Elon Musk’s X is closing Brazil operations amid legal showdown on fake news and hate speech",
    "Japanese living in Brazil after the war imprisoned due to patriotism",
    "Documentary film on Sahrawi women's struggle and suffering under Moroccan occupation screened in Argentina",
    "Thousands of Venezuelans, sympathizers attend rally in Miami demanding Maduro step down",
    "Venezuelans in Caracas and across the world demonstrate to defend opposition’s victory claim",
    "LATAM Crypto Roundup: Bybit Obtains VASP License in Argentina, El Salvador Secures $1.6 Billion …",
    "Social media platform X to shut operations in Brazil, blames top judge for decision",
    "Meghan Markle Wears Johanna Ortiz Set in Colombia",
    "Fleeing Venezuela Before the Elections",
    "This Tiny Fossil Links Wine With The Death of The Dinosaurs",
    "Global warnings after Oropouche virus turns deadly",
    "Venezuelan opposition protests as election dispute drags on",
    "As Venezuela election dispute drags on, opposition coalition protests",
    "X closes operations in Brazil, blames judge’s ‘censorship’ orders",
    "USNS Burlington departs Cartagena, Colombia after fourth Continuing Promise 2024 Mission Stop",
    "Caja del Rio Coalition urges Forest Service to reject LANL transmission line",
    "Woman on nature quest goes missing in San Miguel County backcountry near Norwood",
    "Brazilian television legend Silvio Santos dies at 93",
    "Minister highlights effort in advancing energy transition",
    "Elon Musk’s X to shut operations in Brazil amid bitter legal fight",
    "Chile’s Quijote Films Taps Fabula’s Sergio Karmy to Lead New Growth Plans (EXCLUSIVE)",
    "Devastated mum issues warning about 'silent killer' that killed her son while travelling",
    "X closing operations in Brazil due to judge's content orders",
    "X announces suspension of Brazil operations, alleging ‘censorship orders’ from Supreme Court…",
    "Demonstrations continue in Caracas as international pressure grows on Maduro",
    "Venezuelan opposition holds nationwide rallies against Maduro reelection claim",
    "Bybit Secures VASP License & Boosts Argentinian Crypto Adoption",
    "X to close operations in Brazil after legal battle",
    "'I was imagining my mother in a similar situation'",
    "This Crypto Industry Maven Predicts Spot Solana ETFs Are Coming To The US By 2024-End",
    "Meghan Markle Dancing in Colombia, Prince Harry on Sidelines",
    "Meghan Markle Re-Wears Summer-Ready Jimmy Choo Mules During Visit to Bogota with Prince Harry",
    "Meghan Markle makes powerful 'victim' speech during Colombia tour",
    "Colombia Vice President Says Netflix Series Compelled Her to Invite Prince Harry and Meghan Markle to Visit Her Country",
    "James Pinkerton: Harris' Price Gouging Plan Could Be Campaign Stunt, Or A Slide Toward…",
    "That salsa is spicy: See what happens as a quintet hosts a pedestrian mall fiesta",
    "X suspends business in Brazil over censorship row",
    "Agricultural Experts Push For Climate-Smart Innovations To Ensure Food Security",
    "Elon Musk confirms Brazil X office closure",
    "Musk Vows to Close X’s Brazil Operations, Will Maintain Service",
    "Venezuelan opposition, regime backers hold rival protests",
    "New York Exit: How Much Money Has Aerolneas Argentinas Lost?",
    "Social media platform X to shut down local operations in Brazil: Musk",
    "Sports betting strains family budgets in classes D and E",
    "The Fortress Lives Up To Its Name As The All Blacks Make History Securing 50 Games Unbeaten At Eden Park",
    "Colombia’s Special Jurisdiction for Peace recognises Wiwa people and their ancestral territory as victims of…",
    "Protesters rally in Venezuela’s capital as post-election crisis persists",
    "X says it is closing operations in Brazil immediately following ‘censorship orders’ by judge",
    "Breaking: Elon Musk announces closure of X local operations in Brazil after leftist judge…",
    "X says it is closing operations in Brazil due to judge's content orders",
    "Elon Musk shuts X operations in Brazil ‘effective immediately’",
    "Internet Access Nears Full Coverage in Brazilian Homes",
    "X to wind up operations in Brazil 'effective immediately' due to censorship",
    "Colombia County man arrested on child pornography charges",
    "X is closing its operations in Brazil immediately, but its service will remain live for users",
    "Elon Musk's X shuts down Brazil operations citing arrest ‘threat’ from top judge",
    "Prince Harry and Meghan Markle Meet Colombia’s Invictus Games Team During High-Profile Trip",
    "Meghan Markle wows in most vibrant gown of Colombia tour",
    "X says it is closing Brazilian operations 'effective immediately'",
    "Prince Harry and Meghan Markle arrive at Colombia tour event swamped with soldiers and nuclear…",
    "Musk-owned X to close operations in Brazil 'effective immediately'",
    "X to close operations in Brazil with immediate effect due to 'censorship orders'",
    "Live: Protest in Caracas as Venezuela's opposition call for a world-wide protest",
    "The Hazy Origins Of Peru's Purple Drink, Chicha Morada",
    "Silvio Santos, Brazilian TV Executive and Host, Dies at 93",
    "Prince Harry and Meghan Markle increase security to intense levels on Colombia trip",
    "X to close operations in Brazil 'effective immediately'",
    "‘Keep up the fight:’ Venezuela opposition on eve of protests",
    "Duchess Meghan urges Colombian kids to avoid becoming technology obsessed",
    "Why a Solana ETF Could Be Closer Than You Think",
    "Prince Harry and Meghan Markle in Colombia: Sussexes to make trip close to Meghan's heart",
    "China-Brazil ties: Sichuan's role in 50 years of trade and progress",
    "Venezuelans demonstrate in Amsterdam against President Maduro",
    "Colombia 2024: Falconets to train in Bogota for two weeks",
    "Pacific Datathon region 2024: 50 young Colombians transforming data into solutions",
    "Come to Ecuador, become an expat, stay as long as you want but you can also leave when you want",
    "Beef consumption in Argentina at lowest level in 26 years",
    "The Post Election Role of the Venezuelan Diaspora",
    "Magnitude 3.1 earthquake strikes near Pasto, San Juan de Pasto, Nariño, Colombia",
    "Brazilian entertaining legend Silvio Santos dies at 93",
    "C3 Metals CEO talks pivotal surface access agreement for Khaleesi project – ICYMI",
    "Mike Portnoy On His Renewed Songwriting Chemistry With dream theater: 'We Immediately Felt…",
    "Colombian Locals Confused by Prince Harry and Meghan Markle’s Visit; ‘Are They Here to Help?’",
    "X shuts Brazil operations over 'censorship' orders: Musk",
    "Venezuelan opposition vows to fight 'to the end'",
    "Meghan Markle re-wears summer-ready Jimmy Choo mules during visit to Bogota with Prince Harry",
    "Prince Harry and Meghan Markle land in Colombia for tour-day tour - Duke & Duchess of Sussex…",
    "Elon Musk’s X is closing Brazil operations amid legal showdown on fake news and hate speech",
    "Hurricane Ernesto is downgraded to a tropical storm as it moves through Bermuda",
    "Hezbollah fires rockets at Israel after deadly strike",
    "What to know as India’s medics and women protest the rape and killing of a doctor",
    "U.S. watches closely as Ukrainian forces push into Russia with U.S.-provided arms",
    "Workers from Chicago’s South and West sides make up only 20% of construction labor for DNC",
    "X shuts Brazil operations over 'censorship' orders: Musk",
    "Colombia vice president says Netflix series compelled her to invite Prince Harry and Meghan Markle to visit her country",
    "Venezuelan opposition vows to fight 'to the end'",
    "This crypto industry maven predicts spot Solana ETFs are coming to the US by 2024-end",
    "Prince Harry's cocaine use resurfaces ahead of Colombia trip",
    "Venezuela has arrested thousands in the weeks since controversial election",
    "This Brazilian Athlete Beat the Odds to Win the Same Medal Twice",
    "BHP workers strike at world’s top copper mine in Chile",
    "Workers launch strike at world's largest copper mine in Chile",
    "Meghan Markle's inappropriate outfit on Colombia trip with Prince Harry is so distracting",
    ]
    await sdb.initialize()
    sdb = await SurrealDBStore.afrom_texts(
        dburl="ws://localhost:8000/rpc",
        texts=sentences,db_user="root",db_pass="root",
        embedding=embeddings,
    )
    query = "What is wrong with Prince Harry?"
    await sdb.asimilarity_search(query)
    embeddings = HuggingFaceEmbeddings().embed_query(query)
    await sdb.asimilarity_search_by_vector(embeddings,k=4)
    await sdb.asimilarity_search_with_score(query,k=10,score_threshold=0.6)
    await sdb.asimilarity_search_with_relevance_scores(query,score_threshold=0.5)

asyncio.run(main())


class Indrargos:

    def __init__(self, url):
        self.url = url