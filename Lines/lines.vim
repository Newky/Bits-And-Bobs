"
" Python filetype plugin for running flake8
" Language:     Python (ft=python)
" Maintainer:   Richy Delaney
" Version:      Vim 7 (may work with lower Vim versions, but not tested)
" URL:          http://github.com/Newky/Bits-And-Bobs/
"
" Only do this when not done yet for this buffer
" All of my inspiration for this came from 
" https://github.com/avidal/flake8.vim/
" I copied directly the vim source from that.
"
if exists("b:loaded_lines_ftplugin")
    finish
endif
let b:loaded_lines_ftplugin=1

let s:lines_cmd="lines.py"

if !exists("*LinesExec()")
    function LinesExec()
        if !executable(s:lines_cmd)
            echoerr "File " . s:lines_cmd. " not found. Please install it first."
            return
        endif

        set lazyredraw   " delay redrawing
        cclose           " close any existing cwindows

        " store old grep settings (to restore later)
        let l:old_gfm=&grepformat
        let l:old_gp=&grepprg

        " write any changes before continuing
        if &readonly == 0
            update
        endif

        " perform the grep itself
        let &grepformat="%m:%f:%l"
        let &grepprg=s:lines_cmd
        silent! grep! %

        " restore grep settings
        let &grepformat=l:old_gfm
        let &grepprg=l:old_gp

        " open cwindow
        let has_results=getqflist() != []
        if has_results
            execute 'belowright copen'
            setlocal wrap
            nnoremap <buffer> <silent> c :cclose<CR>
            nnoremap <buffer> <silent> q :cclose<CR>
        endif

        set nolazyredraw
        redraw!

        if has_results == 0
            " Show OK status
            hi Green ctermfg=green
            echohl Green
            echon "No lines over the limit"
            echohl
        endif
    endfunction
endif

" Add mappings, unless the user didn't want this.
" The default mapping is registered under to <F7> by default, unless the user
" remapped it already (or a mapping exists already for <F7>)
if !exists("no_plugin_maps") && !exists("no_flake8_maps")
    if !hasmapto('LinesExec()')
        noremap <buffer> <F7> :call LinesExec()<CR>
        noremap! <buffer> <F7> :call LinesExec()<CR>
    endif
endif
