document.addEventListener('DOMContentLoaded', function () {

    // Function to fetch API version
    /* Facilitates fetching the API version to display on the webpage */
    async function fetchVersion() {
        const versionDisplayElement = document.getElementById('version-display');
        const response = await fetch('/api/get_version');
        const data = await response.json();
        const version_from_data = data.version;
        
        if (versionDisplayElement.textContent === `Version: ${version_from_data}`) {
            versionDisplayElement.textContent = "";  // Obscures version info
        } else {
            versionDisplayElement.textContent = `Version: ${version_from_data}`;  // Displays version info
        }
    }
    
    // Adds an event listener to the Version Info button
    /* Fetches version info when the button is clicked */

    // Function to fetch track data from the server
    /* Fetches track data by page number for pagination */
    async function fetchTrackData(pageNumber) {
        const response = await fetch(`/api/get_tracks?page=${pageNumber}`);
        const data = await response.json();
        return data; // Returns retrieved track data
    }

    // Initializes track data and updates the UI
    /* Loads and displays track data for the first page on page load */
    async function initializeData() {
        const trackinfo = {
            tracks: await fetchTrackData(1),  // Load initial data for the first page
            currentPage: 1,
            totalPages: 2  // Update this as necessary based on your data
        };

        // Populate track information
        /* Populates and displays track information in the table */
        const tbody = document.getElementById('tracks-tbody');
        const currentPageSpan = document.getElementById('current-page');
        const totalPagesSpan = document.getElementById('total-pages');

        currentPageSpan.textContent = trackinfo.currentPage;
        totalPagesSpan.textContent = trackinfo.totalPages;

        trackinfo.tracks.forEach((track, index) => {
            const trackNumber = ((trackinfo.currentPage - 1) * 20) + index + 1;
            const row = document.createElement('tr');

            const trackImageUrl = track.track_image_file || 'URL not available';

            row.innerHTML = `
                <td>${trackNumber}.</td>
                <td>${track.track_title}</td>
                <td>${track.album_title}</td>
                <td>${track.artist_name}</td>
                <td>${track.track_duration}</td>
                <td>${trackImageUrl}</td>
            `;
            tbody.appendChild(row);
        });

        // Navigate between pages
        /* Handles page navigation for track data */
        const prevPageLink = document.getElementById('prev-page');
        const nextPageLink = document.getElementById('next-page');

        prevPageLink.addEventListener('click', async function (e) {
            e.preventDefault();
            /* Loads the previous page of track data */
            if (trackinfo.currentPage > 1) {
                trackinfo.currentPage -= 1;
                trackinfo.tracks = await fetchTrackData(trackinfo.currentPage);
                updateTracksTable(trackinfo);
            }
        });

        nextPageLink.addEventListener('click', async function (e) {
            e.preventDefault();
            /* Loads the next page of track data */
            if (trackinfo.currentPage < trackinfo.totalPages) {
                trackinfo.currentPage += 1;
                trackinfo.tracks = await fetchTrackData(trackinfo.currentPage);
                updateTracksTable(trackinfo);
            }
        });
    }

    // Updates the track table with new data
    /* Clears and repopulates track table with the current page's data */
    async function updateTracksTable(trackinfo) {
        const tbody = document.getElementById('tracks-tbody');
        const currentPageSpan = document.getElementById('current-page');
        
        tbody.innerHTML = "";  // Clear existing rows
        currentPageSpan.textContent = trackinfo.currentPage;

        trackinfo.tracks.forEach((track, index) => {
            const trackNumber = ((trackinfo.currentPage - 1) * 20) + index + 1;
            const row = document.createElement('tr');
            
            const trackImageUrl = track.track_image_file || 'URL not available';

            row.innerHTML = `
                <td>${trackNumber}.</td>
                <td>${track.track_title}</td>
                <td>${track.album_title}</td>
                <td>${track.artist_name}</td>
                <td>${track.track_duration}</td>
                <td>${trackImageUrl}</td>
            `;
            tbody.appendChild(row);
        });
    }

    // Function to show sections
    /* Toggles between home and tracks sections */
    function showSection(section) {
        const homeSection = document.getElementById('home-section');
        const tracksSection = document.getElementById('tracks-section');
        homeSection.style.display = section === 'home' ? 'block' : 'none';
        tracksSection.style.display = section === 'tracks' ? 'block' : 'none';
    }

    // Event listeners for tab navigation
    /* Handles tab navigation to switch sections */
    const homeTab = document.getElementById('home-tab');
    const tracksTab = document.getElementById('tracks-tab');
    homeTab.addEventListener('click', function () {
        showSection('home');
    });

    tracksTab.addEventListener('click', function () {
        showSection('tracks');
        initializeData();
    });

    // Initialize data on page load
    /* Calls the initialization function to load track data */
    fetchVersion();
    showSection('home');
});
