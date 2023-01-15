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
    id: "sinhala_metaphores:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ0NmJkN2RkMWRmYTk0NjY0YjkzYjBjOTQwNjQwMWE1MyRlZWFkMWU5Njc3ZjU0YzYzYWRhOGNjZjQ3NjUxZDQ5MA=="
  },
  apiKey: "OUM3SHNZVUI4SFE1V0kzWVV5REc6MGM3STd6NUNTWTJUQWNoUUt3VGFfdw==",
  index: "sinhala-metaphores"
});

// const connector = new ElasticsearchAPIConnector({
//   host: "https://localhost:9200",
//   index: "sinhala-metaphores"
// });

// const connector = new Client({
//   node: 'https://localhost:9200',
//   auth: {
//     username: 'elastic',
//     password: 'w2gOaqgKdURJJhUCn2pD' 
//   },
//   tls: {
//     ca: fs.readFileSync('./http_ca.crt'),
//     rejectUnauthorized: false
//   }
// })
// INDEX = 'sinhala-metaphores'


const config = {
  searchQuery: {
    search_fields: {
      target: {
        weight: 3
      },
      // plot: {},
      // genre: {},
      // actors: {},
      // directors: {}
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
      // released: {
      //   type: "range",
      //   ranges: [
      //     {
      //       from: "2012-04-07T14:40:04.821Z",
      //       name: "Within the last 10 years"
      //     },
      //     {
      //       from: "1962-04-07T14:40:04.821Z",
      //       to: "2012-04-07T14:40:04.821Z",
      //       name: "10 - 50 years ago"
      //     },
      //     {
      //       to: "1962-04-07T14:40:04.821Z",
      //       name: "More than 50 years ago"
      //     }
      //   ]
      // },
      // imdbRating: {
      //   type: "range",
      //   ranges: [
      //     { from: 1, to: 3, name: "Pants" },
      //     { from: 3, to: 6, name: "Mediocre" },
      //     { from: 6, to: 8, name: "Pretty Good" },
      //     { from: 8, to: 10, name: "Excellent" }
      //   ]
      // }
    }
  },

  autocompleteQuery: {
    results: {
      resultsPerPage: 5,
      search_fields: {
        "target.suggest": {
          weight: 3
        }
      },
      result_fields: {
        target: {
          snippet: {
            size: 100,
            fallback: true
          }
        },
        // url: {
        //   raw: {}
        // }
      }
    },
    suggestions: {
      types: {
        results: { fields: ["movie_completion"] }
      },
      size: 4
    }
  },

  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};

// const connector = new AppSearchAPIConnector({
//   searchKey,
//   engineName,
//   hostIdentifier,
//   endpointBase
// });
// const config = {
//   searchQuery: {
//     facets: buildFacetConfigFromConfig(),
//     ...buildSearchOptionsFromConfig()
//   },
//   autocompleteQuery: buildAutocompleteQueryConfig(),
//   apiConnector: connector,
//   alwaysSearchOnInitialLoad: true
// };


export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox autocompleteSuggestions={false} />}
                  // header={
                  //   <SearchBox
                  //     autocompleteMinimumCharacters={3}
                  //     autocompleteResults={{
                  //       linkTarget: "_blank",
                  //       sectionTitle: "Results",
                  //       titleField: "title",
                  //       urlField: "url",
                  //       shouldTrackClickThrough: true
                  //     }}
                  //     autocompleteSuggestions={true}
                  //     debounceLength={0}
                  //   />
                  // }
                  sideContent={
                    // <div>
                    //   {wasSearched && (
                    //     <Sorting
                    //       label={"Sort by"}
                    //       sortOptions={buildSortOptionsFromConfig()}
                    //     />
                    //   )}
                    //   {getFacetFields().map(field => (
                    //     <Facet key={field} field={field} label={field} />
                    //   ))}
                    // </div>


                    <div>
                    {/* {wasSearched && <Sorting label={"Sort by"} sortOptions={[]} />} */}
                    <Facet key={"1"} field={"Singer.keyword"} label={"Singer"} />
                    <Facet key={"2"} field={"Composer.keyword"} label={"Composer"} />
                    <Facet key={"3"} field={"Lyricist.keyword"} label={"Lyricist"} />
                    {/* <Facet key={"4"} field={"released"} label={"released"} /> */}
                    {/* <Facet key={"4"} field={"imdbRating"} label={"imdb rating"} /> */}
                    </div>

                  }
                  bodyContent={
                    <Results shouldTrackClickThrough={true} />
                    // <Results
                    //   titleField={getConfig().titleField}
                    //   urlField={getConfig().urlField}
                    //   thumbnailField={getConfig().thumbnailField}
                    //   shouldTrackClickThrough={true}
                    // />
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
