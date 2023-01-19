import React from "react";

import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
  ErrorBoundary,
  Facet,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  Sorting,
  WithSearch
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";
// const { Client } = require('@elastic/elasticsearch')


import {
  buildAutocompleteQueryConfig,
  buildFacetConfigFromConfig,
  buildSearchOptionsFromConfig,
  buildSortOptionsFromConfig,
  getConfig,
  getFacetFields
} from "./config/config-helper";


const { hostIdentifier, searchKey, endpointBase, engineName } = getConfig();


const connector = new ElasticsearchAPIConnector({
  cloud: {
    id: "sinhala_metaphores:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ0NmJkN2RkMWRmYTk0NjY0YjkzYjBjOTQwNjQwMWE1MyRlZWFkMWU5Njc3ZjU0YzYzYWRhOGNjZjQ3NjUxZDQ5MA==",
  },
  apiKey: "OUM3SHNZVUI4SFE1V0kzWVV5REc6MGM3STd6NUNTWTJUQWNoUUt3VGFfdw==",
  index: "sinhala-metaphores"
});




const config = {
  searchQuery: {
    search_fields: {
      target: {
        weight: 3
      },
      
    },
    result_fields: {
      Title: {
        snippet: {}
      },
      Singer: {
        snippet: {}
      },
      Composer: {
        snippet: {}
      },
      Lyricist: {
        snippet: {}
      },
      album: {
        snippet: {}
      },
      year: {
        snippet: {}
      },
      Lyrics: {
        snippet: {}
      },
      metaphor: {
        snippet: {}
      },
      source: {
        snippet: {}
      },
      target: {
        snippet: {}
      },
      interpretation: {
        snippet: {}
      }
    },
    disjunctiveFacets: ["Singer.keyword", "Composer.keyword", "Lyricist.keyword"],
    facets: {
      "Singer.keyword": { type: "value" },
      "Composer.keyword": { type: "value" },
      "Lyricist.keyword": { type: "value" }
      
    }
  },


  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};




export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox/>}
                  
                  sideContent={
                    


                    <div>
                    {/* {wasSearched && <Sorting label={"Sort by"} sortOptions={[]} />} */}
                    <Facet key={"1"} field={"Singer.keyword"} label={"Singer"} />
                    <Facet key={"2"} field={"Composer.keyword"} label={"Composer"} />
                    <Facet key={"3"} field={"Lyricist.keyword"} label={"Lyricist"} />
                    
                    </div>

                  }
                  bodyContent={
                    <Results shouldTrackClickThrough={true} />
                    
                  }
                  bodyHeader={
                    <React.Fragment>
                      {wasSearched && <PagingInfo />}
                      {wasSearched && <ResultsPerPage />}
                    </React.Fragment>
                  }
                  bodyFooter={<Paging />}
                />
              </ErrorBoundary>
            </div>
          );
        }}
      </WithSearch>
    </SearchProvider>
  );
}
