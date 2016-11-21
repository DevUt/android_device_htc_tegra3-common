# Include this gypi to include all 'gpu' files
# The parent gyp/gypi file must define
#       'skia_src_path'     e.g. skia/trunk/src
#       'skia_include_path' e.g. skia/trunk/include
#
# The skia build defines these in common_variables.gypi
#
{
  'variables': {
    'skgpu_sources': [
      '<(skia_include_path)/gpu/GrBackendEffectFactory.h',
      '<(skia_include_path)/gpu/GrCacheable.h',
      '<(skia_include_path)/gpu/GrClipData.h',
      '<(skia_include_path)/gpu/GrColor.h',
      '<(skia_include_path)/gpu/GrConfig.h',
      '<(skia_include_path)/gpu/GrContext.h',
      '<(skia_include_path)/gpu/GrContextFactory.h',
      '<(skia_include_path)/gpu/GrCoordTransform.h',
      '<(skia_include_path)/gpu/GrEffect.h',
      '<(skia_include_path)/gpu/GrEffectStage.h',
      '<(skia_include_path)/gpu/GrEffectUnitTest.h',
      '<(skia_include_path)/gpu/GrFontScaler.h',
      '<(skia_include_path)/gpu/GrGlyph.h',
      '<(skia_include_path)/gpu/GrGpuObject.h',
      '<(skia_include_path)/gpu/GrKey.h',
      '<(skia_include_path)/gpu/GrPaint.h',
      '<(skia_include_path)/gpu/GrPathRendererChain.h',
      '<(skia_include_path)/gpu/GrRect.h',
      '<(skia_include_path)/gpu/GrRenderTarget.h',
      '<(skia_include_path)/gpu/GrSurface.h',
      '<(skia_include_path)/gpu/GrTBackendEffectFactory.h',
      '<(skia_include_path)/gpu/GrTexture.h',
      '<(skia_include_path)/gpu/GrTextureAccess.h',
      '<(skia_include_path)/gpu/GrTypes.h',
      '<(skia_include_path)/gpu/GrUserConfig.h',

      '<(skia_include_path)/gpu/gl/GrGLConfig.h',
      '<(skia_include_path)/gpu/gl/GrGLExtensions.h',
      '<(skia_include_path)/gpu/gl/GrGLFunctions.h',
      '<(skia_include_path)/gpu/gl/GrGLInterface.h',

      '<(skia_src_path)/gpu/GrAAHairLinePathRenderer.cpp',
      '<(skia_src_path)/gpu/GrAAHairLinePathRenderer.h',
      '<(skia_src_path)/gpu/GrAAConvexPathRenderer.cpp',
      '<(skia_src_path)/gpu/GrAAConvexPathRenderer.h',
      '<(skia_src_path)/gpu/GrAARectRenderer.cpp',
      '<(skia_src_path)/gpu/GrAARectRenderer.h',
      '<(skia_src_path)/gpu/GrAddPathRenderers_default.cpp',
      '<(skia_src_path)/gpu/GrAllocator.h',
      '<(skia_src_path)/gpu/GrAllocPool.h',
      '<(skia_src_path)/gpu/GrAllocPool.cpp',
      '<(skia_src_path)/gpu/GrAtlas.cpp',
      '<(skia_src_path)/gpu/GrAtlas.h',
      '<(skia_src_path)/gpu/GrBinHashKey.h',
      '<(skia_src_path)/gpu/GrBitmapTextContext.cpp',
      '<(skia_src_path)/gpu/GrBitmapTextContext.h',
      '<(skia_src_path)/gpu/GrBlend.cpp',
      '<(skia_src_path)/gpu/GrBlend.h',
      '<(skia_src_path)/gpu/GrBufferAllocPool.cpp',
      '<(skia_src_path)/gpu/GrBufferAllocPool.h',
      '<(skia_src_path)/gpu/GrCacheable.cpp',
      '<(skia_src_path)/gpu/GrCacheID.cpp',
      '<(skia_src_path)/gpu/GrClipData.cpp',
      '<(skia_src_path)/gpu/GrContext.cpp',
      '<(skia_src_path)/gpu/GrDefaultPathRenderer.cpp',
      '<(skia_src_path)/gpu/GrDefaultPathRenderer.h',
      '<(skia_src_path)/gpu/GrDistanceFieldTextContext.h',
      '<(skia_src_path)/gpu/GrDistanceFieldTextContext.cpp',
      '<(skia_src_path)/gpu/GrDrawState.cpp',
      '<(skia_src_path)/gpu/GrDrawState.h',
      '<(skia_src_path)/gpu/GrDrawTarget.cpp',
      '<(skia_src_path)/gpu/GrDrawTarget.h',
      '<(skia_src_path)/gpu/GrDrawTargetCaps.h',
      '<(skia_src_path)/gpu/GrEffect.cpp',
      '<(skia_src_path)/gpu/GrGeometryBuffer.h',
      '<(skia_src_path)/gpu/GrClipMaskCache.h',
      '<(skia_src_path)/gpu/GrClipMaskCache.cpp',
      '<(skia_src_path)/gpu/GrClipMaskManager.h',
      '<(skia_src_path)/gpu/GrClipMaskManager.cpp',
      '<(skia_src_path)/gpu/GrGpu.cpp',
      '<(skia_src_path)/gpu/GrGpu.h',
      '<(skia_src_path)/gpu/GrGpuObject.cpp',
      '<(skia_src_path)/gpu/GrGpuFactory.cpp',
      '<(skia_src_path)/gpu/GrIndexBuffer.h',
      '<(skia_src_path)/gpu/GrInOrderDrawBuffer.cpp',
      '<(skia_src_path)/gpu/GrInOrderDrawBuffer.h',
      '<(skia_src_path)/gpu/GrLayerCache.cpp',
      '<(skia_src_path)/gpu/GrLayerCache.h',
      '<(skia_src_path)/gpu/GrMemoryPool.cpp',
      '<(skia_src_path)/gpu/GrMemoryPool.h',
      '<(skia_src_path)/gpu/GrOrderedSet.h',
      '<(skia_src_path)/gpu/GrOvalRenderer.cpp',
      '<(skia_src_path)/gpu/GrOvalRenderer.h',
      '<(skia_src_path)/gpu/GrPaint.cpp',
      '<(skia_src_path)/gpu/GrPath.cpp',
      '<(skia_src_path)/gpu/GrPath.h',
      '<(skia_src_path)/gpu/GrPathRendererChain.cpp',
      '<(skia_src_path)/gpu/GrPathRenderer.cpp',
      '<(skia_src_path)/gpu/GrPathRenderer.h',
      '<(skia_src_path)/gpu/GrPathUtils.cpp',
      '<(skia_src_path)/gpu/GrPathUtils.h',
      '<(skia_src_path)/gpu/GrPictureUtils.h',
      '<(skia_src_path)/gpu/GrPictureUtils.cpp',
      '<(skia_src_path)/gpu/GrPlotMgr.h',
      '<(skia_src_path)/gpu/GrRectanizer.h',
      '<(skia_src_path)/gpu/GrRectanizer_pow2.cpp',
      '<(skia_src_path)/gpu/GrRectanizer_pow2.h',
      '<(skia_src_path)/gpu/GrRectanizer_skyline.cpp',
      '<(skia_src_path)/gpu/GrRectanizer_skyline.h',
      '<(skia_src_path)/gpu/GrRedBlackTree.h',
      '<(skia_src_path)/gpu/GrRenderTarget.cpp',
      '<(skia_src_path)/gpu/GrReducedClip.cpp',
      '<(skia_src_path)/gpu/GrReducedClip.h',
      '<(skia_src_path)/gpu/GrResourceCache.cpp',
      '<(skia_src_path)/gpu/GrResourceCache.h',
      '<(skia_src_path)/gpu/GrStencil.cpp',
      '<(skia_src_path)/gpu/GrStencil.h',
      '<(skia_src_path)/gpu/GrStencilAndCoverPathRenderer.cpp',
      '<(skia_src_path)/gpu/GrStencilAndCoverPathRenderer.h',
      '<(skia_src_path)/gpu/GrStencilBuffer.cpp',
      '<(skia_src_path)/gpu/GrStencilBuffer.h',
      '<(skia_src_path)/gpu/GrStrokeInfo.h',
      '<(skia_src_path)/gpu/GrTBSearch.h',
      '<(skia_src_path)/gpu/GrTraceMarker.cpp',
      '<(skia_src_path)/gpu/GrTraceMarker.h',
      '<(skia_src_path)/gpu/GrTracing.h',
      '<(skia_src_path)/gpu/GrSWMaskHelper.cpp',
      '<(skia_src_path)/gpu/GrSWMaskHelper.h',
      '<(skia_src_path)/gpu/GrSoftwarePathRenderer.cpp',
      '<(skia_src_path)/gpu/GrSoftwarePathRenderer.h',
      '<(skia_src_path)/gpu/GrSurface.cpp',
      '<(skia_src_path)/gpu/GrTemplates.h',
      '<(skia_src_path)/gpu/GrTextContext.cpp',
      '<(skia_src_path)/gpu/GrTextContext.h',
      '<(skia_src_path)/gpu/GrTextStrike.cpp',
      '<(skia_src_path)/gpu/GrTextStrike.h',
      '<(skia_src_path)/gpu/GrTextStrike_impl.h',
      '<(skia_src_path)/gpu/GrTexture.cpp',
      '<(skia_src_path)/gpu/GrTextureAccess.cpp',
      '<(skia_src_path)/gpu/GrTHashTable.h',
      '<(skia_src_path)/gpu/GrVertexBuffer.h',

      '<(skia_src_path)/gpu/effects/Gr1DKernelEffect.h',
      '<(skia_src_path)/gpu/effects/GrConfigConversionEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConfigConversionEffect.h',
      '<(skia_src_path)/gpu/effects/GrBezierEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrBezierEffect.h',
      '<(skia_src_path)/gpu/effects/GrConvolutionEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConvolutionEffect.h',
      '<(skia_src_path)/gpu/effects/GrConvexPolyEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConvexPolyEffect.h',
      '<(skia_src_path)/gpu/effects/GrBicubicEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrBicubicEffect.h',
      '<(skia_src_path)/gpu/effects/GrCustomCoordsTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrCustomCoordsTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrDashingEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrDashingEffect.h',
      '<(skia_src_path)/gpu/effects/GrDistanceFieldTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrDistanceFieldTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrDitherEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrDitherEffect.h',
      '<(skia_src_path)/gpu/effects/GrOvalEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrOvalEffect.h',
      '<(skia_src_path)/gpu/effects/GrRRectEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrRRectEffect.h',
      '<(skia_src_path)/gpu/effects/GrSimpleTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrSimpleTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrSingleTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrSingleTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrTextureDomain.cpp',
      '<(skia_src_path)/gpu/effects/GrTextureDomain.h',
      '<(skia_src_path)/gpu/effects/GrTextureStripAtlas.cpp',
      '<(skia_src_path)/gpu/effects/GrTextureStripAtlas.h',

      '<(skia_src_path)/gpu/gl/GrGLAssembleInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLAssembleInterface.h',
      '<(skia_src_path)/gpu/gl/GrGLBufferImpl.cpp',
      '<(skia_src_path)/gpu/gl/GrGLBufferImpl.h',
      '<(skia_src_path)/gpu/gl/GrGLCaps.cpp',
      '<(skia_src_path)/gpu/gl/GrGLCaps.h',
      '<(skia_src_path)/gpu/gl/GrGLContext.cpp',
      '<(skia_src_path)/gpu/gl/GrGLContext.h',
      '<(skia_src_path)/gpu/gl/GrGLCreateNativeInterface_none.cpp',
      '<(skia_src_path)/gpu/gl/GrGLDefaultInterface_none.cpp',
      '<(skia_src_path)/gpu/gl/GrGLDefines.h',
      '<(skia_src_path)/gpu/gl/GrGLEffect.h',
      '<(skia_src_path)/gpu/gl/GrGLVertexEffect.h',
      '<(skia_src_path)/gpu/gl/GrGLExtensions.cpp',
      '<(skia_src_path)/gpu/gl/GrGLIndexBuffer.cpp',
      '<(skia_src_path)/gpu/gl/GrGLIndexBuffer.h',
      '<(skia_src_path)/gpu/gl/GrGLInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLIRect.h',
      '<(skia_src_path)/gpu/gl/GrGLNameAllocator.cpp',
      '<(skia_src_path)/gpu/gl/GrGLNameAllocator.h',
      '<(skia_src_path)/gpu/gl/GrGLNoOpInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLNoOpInterface.h',
      '<(skia_src_path)/gpu/gl/GrGLPath.cpp',
      '<(skia_src_path)/gpu/gl/GrGLPath.h',
      '<(skia_src_path)/gpu/gl/GrGLProgram.cpp',
      '<(skia_src_path)/gpu/gl/GrGLProgram.h',
      '<(skia_src_path)/gpu/gl/GrGLProgramDesc.cpp',
      '<(skia_src_path)/gpu/gl/GrGLProgramDesc.h',
      '<(skia_src_path)/gpu/gl/GrGLProgramEffects.cpp',
      '<(skia_src_path)/gpu/gl/GrGLProgramEffects.h',
      '<(skia_src_path)/gpu/gl/GrGLRenderTarget.cpp',
      '<(skia_src_path)/gpu/gl/GrGLRenderTarget.h',
      '<(skia_src_path)/gpu/gl/GrGLShaderBuilder.cpp',
      '<(skia_src_path)/gpu/gl/GrGLShaderBuilder.h',
      '<(skia_src_path)/gpu/gl/GrGLShaderVar.h',
      '<(skia_src_path)/gpu/gl/GrGLSL.cpp',
      '<(skia_src_path)/gpu/gl/GrGLSL.h',
      '<(skia_src_path)/gpu/gl/GrGLSL_impl.h',
      '<(skia_src_path)/gpu/gl/GrGLStencilBuffer.cpp',
      '<(skia_src_path)/gpu/gl/GrGLStencilBuffer.h',
      '<(skia_src_path)/gpu/gl/GrGLTexture.cpp',
      '<(skia_src_path)/gpu/gl/GrGLTexture.h',
      '<(skia_src_path)/gpu/gl/GrGLUtil.cpp',
      '<(skia_src_path)/gpu/gl/GrGLUtil.h',
      '<(skia_src_path)/gpu/gl/GrGLUniformManager.cpp',
      '<(skia_src_path)/gpu/gl/GrGLUniformManager.h',
      '<(skia_src_path)/gpu/gl/GrGLUniformHandle.h',
      '<(skia_src_path)/gpu/gl/GrGLVertexArray.cpp',
      '<(skia_src_path)/gpu/gl/GrGLVertexArray.h',
      '<(skia_src_path)/gpu/gl/GrGLVertexBuffer.cpp',
      '<(skia_src_path)/gpu/gl/GrGLVertexBuffer.h',
      '<(skia_src_path)/gpu/gl/GrGpuGL.cpp',
      '<(skia_src_path)/gpu/gl/GrGpuGL.h',
      '<(skia_src_path)/gpu/gl/GrGpuGL_program.cpp',

      # Sk files
      '<(skia_include_path)/gpu/SkGpuDevice.h',
      '<(skia_include_path)/gpu/SkGr.h',
      '<(skia_include_path)/gpu/SkGrPixelRef.h',
      '<(skia_include_path)/gpu/SkGrTexturePixelRef.h',

      '<(skia_include_path)/gpu/gl/SkGLContextHelper.h',

      '<(skia_src_path)/gpu/SkGpuDevice.cpp',
      '<(skia_src_path)/gpu/SkGr.cpp',
      '<(skia_src_path)/gpu/SkGrFontScaler.cpp',
      '<(skia_src_path)/gpu/SkGrPixelRef.cpp',
      '<(skia_src_path)/gpu/SkGrTexturePixelRef.cpp',

      '<(skia_src_path)/image/SkImage_Gpu.cpp',
      '<(skia_src_path)/image/SkSurface_Gpu.cpp',

      '<(skia_src_path)/gpu/gl/SkGLContextHelper.cpp'
    ],
    'skgpu_native_gl_sources': [
      '<(skia_src_path)/gpu/gl/GrGLDefaultInterface_native.cpp',
      '<(skia_src_path)/gpu/gl/mac/GrGLCreateNativeInterface_mac.cpp',
      '<(skia_src_path)/gpu/gl/win/GrGLCreateNativeInterface_win.cpp',
      '<(skia_src_path)/gpu/gl/unix/GrGLCreateNativeInterface_unix.cpp',
      '<(skia_src_path)/gpu/gl/iOS/GrGLCreateNativeInterface_iOS.cpp',
      '<(skia_src_path)/gpu/gl/android/GrGLCreateNativeInterface_android.cpp',

      # Sk files
      '<(skia_include_path)/gpu/gl/SkNativeGLContext.h',
      '<(skia_src_path)/gpu/gl/mac/SkNativeGLContext_mac.cpp',
      '<(skia_src_path)/gpu/gl/nacl/SkNativeGLContext_nacl.cpp',
      '<(skia_src_path)/gpu/gl/win/SkNativeGLContext_win.cpp',
      '<(skia_src_path)/gpu/gl/unix/SkNativeGLContext_unix.cpp',
      '<(skia_src_path)/gpu/gl/android/SkNativeGLContext_android.cpp',
      '<(skia_src_path)/gpu/gl/iOS/SkNativeGLContext_iOS.mm',
    ],
    'skgpu_mesa_gl_sources': [
      '<(skia_src_path)/gpu/gl/mesa/GrGLCreateMesaInterface.cpp',

      # Sk files
      '<(skia_include_path)/gpu/gl/SkMesaGLContext.h',
      '<(skia_src_path)/gpu/gl/mesa/SkMesaGLContext.cpp',
    ],
    'skgpu_angle_gl_sources': [
      '<(skia_src_path)/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',

      # Sk files
      '<(skia_include_path)/gpu/gl/SkANGLEGLContext.h',
      '<(skia_src_path)/gpu/gl/angle/SkANGLEGLContext.cpp',
    ],
    'skgpu_debug_gl_sources': [
      '<(skia_src_path)/gpu/gl/debug/GrGLCreateDebugInterface.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrFakeRefObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrBufferObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrBufferObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrFBBindableObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrRenderBufferObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrTextureObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrTextureObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrTextureUnitObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrTextureUnitObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrFrameBufferObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrFrameBufferObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrShaderObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrShaderObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrProgramObj.h',
      '<(skia_src_path)/gpu/gl/debug/GrProgramObj.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrDebugGL.h',
      '<(skia_src_path)/gpu/gl/debug/GrDebugGL.cpp',
      '<(skia_src_path)/gpu/gl/debug/GrVertexArrayObj.h',

      # Sk files
      '<(skia_include_path)/gpu/gl/SkDebugGLContext.h',
      '<(skia_src_path)/gpu/gl/debug/SkDebugGLContext.cpp',
    ],
    'skgpu_null_gl_sources': [
      '<(skia_src_path)/gpu/gl/GrGLCreateNullInterface.cpp',

      # Sk files
      '<(skia_include_path)/gpu/gl/SkNullGLContext.h',
      '<(skia_src_path)/gpu/gl/SkNullGLContext.cpp',
    ],
  },
}
