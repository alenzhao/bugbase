




<!DOCTYPE html>
<html lang="en" class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>OTUsearch/trim_alignment_by_primers.py at master · danknights/OTUsearch · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="danknights/OTUsearch" name="twitter:title" /><meta content="Contribute to OTUsearch development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/2553315?v=2&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/2553315?v=2&amp;s=400" property="og:image" /><meta content="danknights/OTUsearch" property="og:title" /><meta content="https://github.com/danknights/OTUsearch" property="og:url" /><meta content="Contribute to OTUsearch development by creating an account on GitHub." property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="80652355:4A69:35602D:53E52CC5" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="5sBMA/GrrhLmlrKTe1u5TIUyALAxPEWARj1ggcpMW3ljC6/8T4vmltTGx0clvqB/NenJlOWd/ZURyZl3aZ8O4Q==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-bafb7d79cb7c6afd58c1a71e64771d2ad89aecab.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-b855c0b37e346d3dac214385acbf7f00a78096db.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="99c3cb38b138149e0f769b076d8f3e85">

      
  <meta name="description" content="Contribute to OTUsearch development by creating an account on GitHub.">


  <meta content="2553315" name="octolytics-dimension-user_id" /><meta content="danknights" name="octolytics-dimension-user_login" /><meta content="18739588" name="octolytics-dimension-repository_id" /><meta content="danknights/OTUsearch" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="18739588" name="octolytics-dimension-repository_network_root_id" /><meta content="danknights/OTUsearch" name="octolytics-dimension-repository_network_root_nwo" />

  <link href="https://github.com/danknights/OTUsearch/commits/master.atom" rel="alternate" title="Recent Commits to OTUsearch:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fdanknights%2FOTUsearch%2Fblob%2Fmaster%2Fbin%2Ftrim_alignment_by_primers.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
          <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
    data-repo="danknights/OTUsearch"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="danknights/OTUsearch">

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked">
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global">
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">


  <li>
      <a href="/login?return_to=%2Fdanknights%2FOTUsearch"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/danknights/OTUsearch/stargazers">
      0
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fdanknights%2FOTUsearch"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/danknights/OTUsearch/network" class="social-count">
        1
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/danknights" class="url fn" itemprop="url" rel="author"><span itemprop="title">danknights</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/danknights/OTUsearch" class="js-current-repository js-repo-home-link">OTUsearch</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders" data-issue-count-url="/danknights/OTUsearch/issues/counts">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/danknights/OTUsearch" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /danknights/OTUsearch">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/danknights/OTUsearch/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /danknights/OTUsearch/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class="js-issue-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/danknights/OTUsearch/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /danknights/OTUsearch/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class="js-pull-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/danknights/OTUsearch/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /danknights/OTUsearch/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/danknights/OTUsearch/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /danknights/OTUsearch/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/danknights/OTUsearch.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/danknights/OTUsearch.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/danknights/OTUsearch" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/danknights/OTUsearch" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/danknights/OTUsearch/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download danknights/OTUsearch as a zip file"
                   title="Download danknights/OTUsearch as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/danknights/OTUsearch/blob/5d35a657561ad3877cada7664e1b0e1acdc50360/bin/trim_alignment_by_primers.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:05578bc3f5052d59ec907c92c7025182 -->

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/danknights/OTUsearch/blob/master/bin/trim_alignment_by_primers.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/danknights/OTUsearch/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="bin/trim_alignment_by_primers.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/danknights/OTUsearch" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">OTUsearch</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/danknights/OTUsearch/tree/master/bin" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">bin</span></a></span><span class="separator"> / </span><strong class="final-path">trim_alignment_by_primers.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="danknights" class="main-avatar" data-user="2553315" height="24" src="https://avatars3.githubusercontent.com/u/2553315?v=2&amp;s=48" width="24" />
      <span class="author"><a href="/danknights" rel="author">danknights</a></span>
      <time datetime="2014-04-14T15:06:23-05:00" is="relative-time">April 14, 2014</time>
      <div class="commit-title">
          <a href="/danknights/OTUsearch/commit/4d83ad5e683f0d70738369d303c0bb39628df695" class="message" data-pjax="true" title="moved scripts to bin">moved scripts to bin</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong>  contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="danknights" data-user="2553315" height="24" src="https://avatars3.githubusercontent.com/u/2553315?v=2&amp;s=48" width="24" />
            <a href="/danknights">danknights</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>113 lines (96 sloc)</span>
          <span class="meta-divider"></span>
        <span>3.892 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/danknights/OTUsearch/raw/master/bin/trim_alignment_by_primers.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/danknights/OTUsearch/blame/master/bin/trim_alignment_by_primers.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/danknights/OTUsearch/commits/master/bin/trim_alignment_by_primers.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->


            <a class="octicon-button disabled tooltipped tooltipped-w" href="#"
               aria-label="You must be signed in to make or propose changes"><span class="octicon octicon-pencil"></span></a>

          <a class="octicon-button danger disabled tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python">
      
<table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-line-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-line-code js-file-line"><span class="c"># Truncate alignment using forward and reverse primers</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-line-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-line-code js-file-line"><span class="c"># </span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-line-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-line-code js-file-line"><span class="c"># Note: this currently assumes primer will be present ungapped in alignment</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-line-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-line-code js-file-line"><span class="c"># Also assumes 7 bases of primer are sufficient to resolve position</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-line-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-line-code js-file-line"><span class="c"># Also can&#39;t handle ambiguous bases</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-line-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-line-code js-file-line"><span class="c"># </span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-line-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-line-code js-file-line"><span class="c"># usage:</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-line-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-line-code js-file-line"><span class="c"># python trim_alignment_by_primers.py -i alignment.fasta --forward GTGCCAGCMGCCGCGGTAA --reverse GGACTACHVGGGTWTCTAAT</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-line-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-line-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-line-code js-file-line"><span class="kn">from</span> <span class="nn">cogent.core.moltype</span> <span class="kn">import</span> <span class="n">DNA</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-line-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-line-code js-file-line"><span class="kn">from</span> <span class="nn">cogent</span> <span class="kn">import</span> <span class="n">LoadSeqs</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-line-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-line-code js-file-line"><span class="kn">import</span> <span class="nn">sys</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-line-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-line-code js-file-line"><span class="kn">import</span> <span class="nn">os</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-line-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-line-code js-file-line"><span class="kn">import</span> <span class="nn">optparse</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-line-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-line-code js-file-line"><span class="n">PRIMER_TRIM_LEN</span> <span class="o">=</span> <span class="mi">6</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-line-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-line-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-line-code js-file-line"><span class="k">def</span> <span class="nf">ambiguousMatchChar</span><span class="p">(</span><span class="n">char1</span><span class="p">,</span><span class="n">char2</span><span class="p">,</span><span class="n">accept_both_ambiguous</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span>	</td>
      </tr>
      <tr>
        <td id="L18" class="blob-line-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-line-code js-file-line">	<span class="sd">&quot;&quot;&quot;Matches two DNA characters accounting for ambiguous bases in one or both.</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-line-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-line-code js-file-line"><span class="sd">	&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-line-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-line-code js-file-line">	<span class="n">ambig_codes</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;K&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;G&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;M&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;C&#39;</span><span class="p">]),</span> <span class="s">&#39;R&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">]),</span> <span class="s">&#39;Y&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;S&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">]),</span> <span class="s">&#39;W&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;B&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;V&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">]),</span> <span class="s">&#39;H&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;D&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;N&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">,</span><span class="s">&#39;C&#39;</span><span class="p">,</span><span class="s">&#39;G&#39;</span><span class="p">,</span><span class="s">&#39;T&#39;</span><span class="p">]),</span> <span class="s">&#39;A&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;A&#39;</span><span class="p">]),</span> <span class="s">&#39;C&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;C&#39;</span><span class="p">]),</span> <span class="s">&#39;G&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;G&#39;</span><span class="p">]),</span> <span class="s">&#39;T&#39;</span><span class="p">:</span><span class="nb">set</span><span class="p">([</span><span class="s">&#39;T&#39;</span><span class="p">])}</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-line-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-line-code js-file-line">	<span class="n">set1</span> <span class="o">=</span> <span class="n">ambig_codes</span><span class="p">[</span><span class="n">char1</span><span class="p">]</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-line-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-line-code js-file-line">	<span class="n">set2</span> <span class="o">=</span> <span class="n">ambig_codes</span><span class="p">[</span><span class="n">char2</span><span class="p">]</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-line-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="ow">not</span> <span class="n">accept_both_ambiguous</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">set1</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">set2</span><span class="p">))</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-line-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-line-code js-file-line">		<span class="k">return</span> <span class="bp">False</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-line-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">set1</span><span class="o">.</span><span class="n">intersection</span><span class="p">(</span><span class="n">set2</span><span class="p">))</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-line-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-line-code js-file-line">		<span class="k">return</span> <span class="bp">True</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-line-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-line-code js-file-line">	<span class="k">return</span> <span class="bp">False</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-line-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L29" class="blob-line-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-line-code js-file-line"><span class="k">def</span> <span class="nf">findMotif</span><span class="p">(</span><span class="n">seq</span><span class="p">,</span><span class="n">motif</span><span class="p">,</span><span class="n">end_pos</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>	</td>
      </tr>
      <tr>
        <td id="L30" class="blob-line-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-line-code js-file-line">	<span class="sd">&quot;&quot;&quot;Determines the index of the motif (a string) in the sequence object seq</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-line-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-line-code js-file-line"><span class="sd">	   ignoring gaps in seq and accounting for ambiguous bases   </span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-line-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-line-code js-file-line"><span class="sd">	&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-line-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-line-code js-file-line">	</td>
      </tr>
      <tr>
        <td id="L34" class="blob-line-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-line-code js-file-line">	<span class="c"># check each starting position</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-line-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-line-code js-file-line">	<span class="n">degap</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">seq</span><span class="o">.</span><span class="n">degap</span><span class="p">())</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-line-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-line-code js-file-line">	<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">degap</span><span class="p">)</span><span class="o">-</span><span class="nb">len</span><span class="p">(</span><span class="n">motif</span><span class="p">)):</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-line-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-line-code js-file-line">		<span class="n">j</span> <span class="o">=</span> <span class="mi">0</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-line-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-line-code js-file-line">		<span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">motif</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ambiguousMatchChar</span><span class="p">(</span><span class="n">motif</span><span class="p">[</span><span class="n">j</span><span class="p">],</span><span class="n">degap</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="n">j</span><span class="p">]):</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-line-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-line-code js-file-line">			<span class="n">j</span> <span class="o">+=</span> <span class="mi">1</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-line-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-line-code js-file-line">		<span class="k">if</span> <span class="n">j</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">motif</span><span class="p">):</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-line-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-line-code js-file-line">			<span class="k">if</span> <span class="n">end_pos</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-line-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-line-code js-file-line">				<span class="k">return</span> <span class="n">seq</span><span class="o">.</span><span class="n">gapMaps</span><span class="p">()[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">motif</span><span class="p">)]</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-line-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-line-code js-file-line">			<span class="k">return</span> <span class="n">seq</span><span class="o">.</span><span class="n">gapMaps</span><span class="p">()[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">]</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-line-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-line-code js-file-line">	<span class="k">return</span> <span class="o">-</span><span class="mi">1</span>	</td>
      </tr>
      <tr>
        <td id="L45" class="blob-line-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L46" class="blob-line-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-line-code js-file-line"><span class="k">def</span> <span class="nf">get_opts</span><span class="p">():</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-line-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-line-code js-file-line">    <span class="n">p</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="p">()</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-line-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-line-code js-file-line">    <span class="n">p</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-i&quot;</span><span class="p">,</span> <span class="s">&quot;--input&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;string&quot;</span><span class="p">,</span> \</td>
      </tr>
      <tr>
        <td id="L49" class="blob-line-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-line-code js-file-line">        <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Input alignment file [required].&quot;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-line-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-line-code js-file-line">    <span class="n">p</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-o&quot;</span><span class="p">,</span> <span class="s">&quot;--output&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;string&quot;</span><span class="p">,</span> \</td>
      </tr>
      <tr>
        <td id="L51" class="blob-line-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-line-code js-file-line">        <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Output alignment file [default append _degap_trim].&quot;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-line-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-line-code js-file-line">    <span class="n">p</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--forward&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;string&quot;</span><span class="p">,</span> \</td>
      </tr>
      <tr>
        <td id="L53" class="blob-line-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-line-code js-file-line">        <span class="n">default</span><span class="o">=</span><span class="s">&#39;GTGCCAGCMGCCGCGGTAA&#39;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Forward primer [default </span><span class="si">%d</span><span class="s">efault]&quot;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-line-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-line-code js-file-line">    <span class="n">p</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--reverse&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;string&quot;</span><span class="p">,</span> \</td>
      </tr>
      <tr>
        <td id="L55" class="blob-line-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-line-code js-file-line">        <span class="n">default</span><span class="o">=</span><span class="s">&#39;GGACTACHVGGGTWTCTAAT&#39;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Forward primer [default </span><span class="si">%d</span><span class="s">efault]&quot;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-line-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-line-code js-file-line">    <span class="n">p</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--verbose&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> \</td>
      </tr>
      <tr>
        <td id="L57" class="blob-line-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-line-code js-file-line">        <span class="n">help</span><span class="o">=</span><span class="s">&quot;Print all output.&quot;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-line-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-line-code js-file-line">    <span class="n">opts</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">parse_args</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-line-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L60" class="blob-line-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-line-code js-file-line">    <span class="k">return</span> <span class="n">opts</span><span class="p">,</span> <span class="n">args</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-line-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L62" class="blob-line-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-line-code js-file-line"><span class="k">def</span> <span class="nf">check_opts</span><span class="p">(</span><span class="n">opts</span><span class="p">):</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-line-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">input</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-line-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-line-code js-file-line">		<span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n\n</span><span class="s">Please include an input reference alignment.&#39;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-line-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-line-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-line-code js-file-line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-line-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-line-code js-file-line">	<span class="n">opts</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">get_opts</span><span class="p">()</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-line-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-line-code js-file-line">	<span class="n">check_opts</span><span class="p">(</span><span class="n">opts</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-line-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-line-code js-file-line">	</td>
      </tr>
      <tr>
        <td id="L70" class="blob-line-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-line-code js-file-line">	<span class="c"># load alignment</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-line-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-line-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-line-code js-file-line">		<span class="k">print</span> <span class="s">&#39;Loading seqs...&#39;</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-line-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-line-code js-file-line">	<span class="n">ref_fp</span> <span class="o">=</span> <span class="n">opts</span><span class="o">.</span><span class="n">input</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-line-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-line-code js-file-line">	<span class="n">ref</span> <span class="o">=</span> <span class="n">LoadSeqs</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="n">ref_fp</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-line-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-line-code js-file-line">	</td>
      </tr>
      <tr>
        <td id="L76" class="blob-line-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-line-code js-file-line">	<span class="n">out_fp</span> <span class="o">=</span> <span class="n">opts</span><span class="o">.</span><span class="n">output</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-line-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-line-code js-file-line">	<span class="n">base</span><span class="p">,</span> <span class="n">ext</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">ref_fp</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-line-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-line-code js-file-line">	<span class="n">out_fp_degap</span> <span class="o">=</span> <span class="n">base</span>  <span class="o">+</span> <span class="s">&#39;_degap&#39;</span> <span class="o">+</span> <span class="n">ext</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-line-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="n">out_fp</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-line-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-line-code js-file-line">		<span class="n">base</span><span class="p">,</span> <span class="n">ext</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">ref_fp</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-line-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-line-code js-file-line">		<span class="n">out_fp</span> <span class="o">=</span> <span class="n">base</span>  <span class="o">+</span> <span class="s">&#39;_degap_trim&#39;</span> <span class="o">+</span> <span class="n">ext</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-line-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L83" class="blob-line-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-line-code js-file-line">	<span class="c"># trim primers and reverse-complement reverse primer</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-line-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-line-code js-file-line">	<span class="n">forward_primer_full</span> <span class="o">=</span> <span class="n">opts</span><span class="o">.</span><span class="n">forward</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-line-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-line-code js-file-line">	<span class="n">forward_primer</span> <span class="o">=</span> <span class="n">forward_primer_full</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-line-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-line-code js-file-line">	<span class="n">reverse_primer</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">DNA</span><span class="o">.</span><span class="n">makeSequence</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">reverse</span><span class="p">)</span><span class="o">.</span><span class="n">rc</span><span class="p">())</span></td>
      </tr>
      <tr>
        <td id="L87" class="blob-line-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-line-code js-file-line">	</td>
      </tr>
      <tr>
        <td id="L88" class="blob-line-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-line-code js-file-line">	<span class="c"># find start and end of primer in first ref sequence</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-line-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-line-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-line-code js-file-line">		<span class="k">print</span> <span class="s">&#39;Searching for primers...&#39;</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-line-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-line-code js-file-line">	<span class="n">primers_found</span> <span class="o">=</span> <span class="bp">False</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-line-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-line-code js-file-line">	<span class="n">count</span> <span class="o">=</span> <span class="mi">0</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-line-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-line-code js-file-line">	<span class="n">seq_names</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">Names</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-line-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-line-code js-file-line">	<span class="k">while</span> <span class="ow">not</span> <span class="n">primers_found</span> <span class="ow">and</span> <span class="n">count</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref</span><span class="p">):</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-line-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-line-code js-file-line">		</td>
      </tr>
      <tr>
        <td id="L96" class="blob-line-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-line-code js-file-line">		<span class="n">start_index</span> <span class="o">=</span> <span class="n">findMotif</span><span class="p">(</span><span class="n">ref</span><span class="o">.</span><span class="n">getGappedSeq</span><span class="p">(</span><span class="n">seq_names</span><span class="p">[</span><span class="n">count</span><span class="p">]),</span> <span class="n">forward_primer</span><span class="p">,</span> <span class="n">end_pos</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-line-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-line-code js-file-line">		<span class="n">end_index</span> <span class="o">=</span> <span class="n">findMotif</span><span class="p">(</span><span class="n">ref</span><span class="o">.</span><span class="n">getGappedSeq</span><span class="p">(</span><span class="n">seq_names</span><span class="p">[</span><span class="n">count</span><span class="p">]),</span> <span class="n">reverse_primer</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-line-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-line-code js-file-line">		<span class="n">primers_found</span> <span class="o">=</span> <span class="n">start_index</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">end_index</span> <span class="o">&gt;</span> <span class="mi">0</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-line-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-line-code js-file-line">		<span class="n">count</span> <span class="o">+=</span> <span class="mi">1</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-line-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-line-code js-file-line">		<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-line-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-line-code js-file-line">			<span class="k">print</span> <span class="s">&quot;Primers not found in sequence&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">count</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;...&#39;</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-line-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="ow">not</span> <span class="n">primers_found</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-line-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-line-code js-file-line">		<span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n\n</span><span class="s">Primers not found in ref seqs.&#39;</span><span class="p">)</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-line-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-line-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-line-code js-file-line">	<span class="n">ref</span> <span class="o">=</span> <span class="n">ref</span><span class="p">[</span><span class="n">start_index</span><span class="p">:</span><span class="n">end_index</span><span class="p">]</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-line-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-line-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-line-code js-file-line">	<span class="c"># drop any all-gap positions in alignment</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-line-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-line-code js-file-line">	<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-line-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-line-code js-file-line">		<span class="k">print</span> <span class="s">&#39;Removing extraneous gaps...&#39;</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-line-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-line-code js-file-line">	<span class="n">ref</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">omitGapPositions</span><span class="p">()</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-line-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-line-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L112" class="blob-line-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-line-code js-file-line">	<span class="n">ref</span><span class="o">.</span><span class="n">writeToFile</span><span class="p">(</span><span class="n">out_fp</span><span class="p">)</span></td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.02438s from github-fe116-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-12d5fda141e78e513749dddbc56445fe172cbd9a.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-cd771a23c0ba85a1956f1a2611664cf19a9c6554.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

